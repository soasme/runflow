"""
This module is a fork of amplify-education/python-hcl2.

Some reasons not using python-hcl2:

* It returns Dict, instead of an AST. For the Runflow's use case, we
  need to populate some fields in the runtime.

* The library seems problematic for a while:
  * It cannot parse exp values: 1e7 => lark.exceptions.UnexpectedToken.
  * It cannot transform full splat:
    a=b[*].1 => {'a': Tree('full_splat_expr_term', ['b', 1])}
  * It turns attribute values to a list: a = 1 => "a": [1].

* I want something like `$datetime:datetime(year, month, date)` in HCL2.
"""

import itertools
import json
import operator
import os
import re
import textwrap
from datetime import datetime
from functools import singledispatch
from os.path import dirname
from typing import Any, Dict, List, Set, Union

from dateutil.parser import parse as parse_datetime
from lark import Discard, Lark, Transformer

from runflow.errors import RunflowReferenceError
from runflow.utils import import_module

HEREDOC_PATTERN = re.compile(
    r"<<-?([a-zA-Z][a-zA-Z0-9._-]+)\n((.|\n)*?)\n\s*\1", re.S
)

INTERPOLATION = re.compile(r'\${ *((?:"(?:[^"\\]|\\.)*"|[^}"]+)+) *}')


def parse_template(string):
    result = []
    previous = 0

    for interpolation_match in INTERPOLATION.finditer(string):
        start, end = interpolation_match.span()

        if previous != start:
            result.append(StringLit(string[previous:start]))

        expr = interpolation_match.group(1)
        result.append(loads(expr, start="eval"))
        previous = end

    if not result:
        return StringLit(string)

    if previous != len(string):
        result.append(StringLit(string[previous:]))

    return JoinedStr(result)


class Module(dict):
    pass


class StringLit(str):
    pass


class JoinedStr:
    def __init__(self, elements):
        self.elements = elements

    def __repr__(self):
        return "<JoinedStr>"

    def __eq__(self, o):
        return isinstance(o, JoinedStr) and o.elements == self.elements


class Attribute(dict):
    def __init__(self, key, value):
        self.key = key
        self.value = value
        super().__init__({key: value})

    def merge_to(self, res):
        res = dict(res)
        res.update(self)
        return res


class Block(dict):
    def merge_to(self, res):
        res = dict(res)
        for key, value in self.items():
            key = str(key)

            if key not in res:
                res[key] = [value]
                continue

            if not isinstance(res[key], list):
                res[key] = [res[key], value]
                continue

            if isinstance(value, list):
                res[key].extend(value)
            else:
                res[key].append(value)

        return res


class Interpolation(str):
    def __init__(self, expr):
        super().__init__()
        self.expr = expr
        self.value = "${%s}" % expr

    def __str__(self):
        return self.value

    def __repr__(self):
        return self.value

    def __eq__(self, o):
        return isinstance(o, Interpolation) and self.expr == o.expr


class Identifier(str):
    pass


class GetIndex:
    def __init__(self, expr, index):
        self.expr = expr
        self.index = index
        self.value = "%s[%s]" % (self.expr, self.index)

    def __str__(self):
        return self.value

    def __repr__(self):
        return self.value

    def __eq__(self, o):
        return (
            isinstance(o, GetIndex)
            and self.expr == o.expr
            and self.index == o.index
        )

    @property
    def attr_chain(self):
        chain = []
        extract_attr_chain(self, chain)
        return chain


class GetAttr:
    def __init__(self, expr, attr):
        self.expr = expr
        self.attr = attr
        self.value = "%s.%s" % (self.expr, self.attr)

    def __str__(self):
        return self.value

    def __repr__(self):
        return self.value

    def __eq__(self, o):
        return (
            isinstance(o, GetAttr)
            and self.expr == o.expr
            and self.attr == o.attr
        )

    @property
    def attr_chain(self):
        chain = []
        extract_attr_chain(self, chain)
        return chain


@singledispatch
def extract_attr_chain(ast, chain):
    chain.append(ast)


@extract_attr_chain.register
def _(ast: GetAttr, chain):
    extract_attr_chain(ast.expr, chain)
    chain.append(ast.attr)


@extract_attr_chain.register
def _(ast: GetIndex, chain):
    extract_attr_chain(ast.expr, chain)
    chain.append(ast.index)


class Splat:
    def __init__(self, array, elements):
        self.array = array
        self.elements = elements

    def __repr__(self):
        return "%s.*.%s" % (
            self.array,
            ".".join([str(e) for e in self.elements]),
        )

    def __eq__(self, o):
        return (
            isinstance(o, Splat)
            and self.array == o.array
            and self.elements == o.elements
        )


class Call:
    def __init__(self, func_name, args):
        self.func_name = func_name
        self.args = args

    def __repr__(self):
        return "%s(%s)" % (self.func_name, ",".join(str(a) for a in self.args))

    def __eq__(self, o):
        return (
            isinstance(o, Call)
            and self.func_name == o.func_name
            and self.args == o.args
        )


class Conditional:
    def __init__(self, predicate, true_expr, false_expr):
        self.predicate = predicate
        self.true_expr = true_expr
        self.false_expr = false_expr

    def __repr__(self):
        return "%s ? %s : %s" % (
            self.predicate,
            self.true_expr,
            self.false_expr,
        )

    def __eq__(self, o):
        return (
            isinstance(o, Conditional)
            and self.predicate == o.predicate
            and self.true_expr == o.true_expr
            and self.false_expr == o.false_expr
        )


class Operation:
    def __init__(self, elements):
        self.elements = elements

    def __repr__(self):
        return "(%s)" % ("".join([str(e) for e in self.elements]))

    def __eq__(self, o):
        return isinstance(o, Operation) and self.elements == o.elements


class ListExpr:
    def __init__(self, element_id, array, element, condition):
        self.element_id = element_id
        self.array = array
        self.element = element
        self.condition = condition

    def __repr__(self):
        return "[for %s in %s: %s%s]" % (
            (
                ",".join(self.element_id)
                if isinstance(self.element_id, tuple)
                else self.element_id
            ),
            self.array,
            self.element,
            f" if {self.condition}" if self.condition else "",
        )

    def __eq__(self, o):
        return (
            isinstance(o, ListExpr)
            and self.element_id == o.element_id
            and self.array == o.array
            and self.element == o.element
            and self.condition == o.condition
        )


# pylint: disable=too-many-arguments
class DictExpr:
    def __init__(self, element_id, array, key, value, condition):
        self.array = array
        self.element_id = element_id
        self.key = key
        self.value = value
        self.condition = condition

    def __repr__(self):
        return "{for %s in %s: %s => %s%s}" % (
            (
                ",".join(self.element_id)
                if isinstance(self.element_id, tuple)
                else self.element_id
            ),
            self.array,
            self.key,
            self.value,
            f" if {self.condition}" if self.condition else "",
        )

    def __eq__(self, o):
        return (
            isinstance(o, DictExpr)
            and self.element_id == o.element_id
            and self.array == o.array
            and self.key == o.key
            and self.value == o.value
            and self.condition == o.condition
        )


class Not:
    def __init__(self, expr):
        self.expr = expr

    def __repr__(self):
        return "(!%s)" % self.expr

    def __eq__(self, o):
        return isinstance(o, Not) and self.expr == o.expr


def strip_new_line_tokens(args: List) -> List:
    return [
        arg for arg in args if arg != "\n" and not isinstance(arg, Discard)
    ]


# pylint: disable=too-many-public-methods,no-self-use
class AstTransformer(Transformer):
    def module(self, args: List) -> Dict:
        args = strip_new_line_tokens(args)
        return Module(args[0])

    def eval(self, args: List) -> Dict:
        return args[0]

    def quoted_template_expr(self, args: Any):
        return parse_template(args[0])

    def string_lit(self, args: Any):
        return StringLit(args[0])

    # pylint: disable=invalid-name
    def STRING_LIT(self, args: Any):
        return self.strip_quotes("".join([str(arg) for arg in args]))

    def _heredoc_template(self, args: List) -> str:
        match = HEREDOC_PATTERN.match(str(args[0]))
        if not match:
            raise RuntimeError("Invalid Heredoc token: %s" % args[0])
        return match.group(2)

    def heredoc_template(self, args: List) -> str:
        return parse_template(self._heredoc_template(args))

    def heredoc_template_trim(self, args: List) -> str:
        return parse_template(textwrap.dedent(self._heredoc_template(args)))

    def float_lit(self, args: List) -> float:
        return float("".join([str(arg) for arg in args]))

    def int_lit(self, args: List) -> int:
        return int("".join([str(arg) for arg in args]))

    def expr_term(self, args: List) -> Any:
        args = strip_new_line_tokens(args)
        if args[0] == "true":
            return True
        if args[0] == "false":
            return False
        if args[0] == "null":
            return None
        if args[0] == "(":
            return args[1]
        return args[0]

    def attribute(self, args: List) -> Attribute:
        key = str(args[0])
        if key.startswith('"') and key.endswith('"'):
            key = key[1:-1]
        value = self.to_string_dollar(args[1])
        return Attribute(key, value)

    def block(self, args: List) -> Block:
        args = strip_new_line_tokens(args)
        if isinstance(args[-1], str):
            args.append({})

        result: Dict[str, Any] = {}
        current_level = result
        for arg in args[0:-2]:
            current_level[self.strip_quotes(arg)] = {}
            current_level = current_level[self.strip_quotes(arg)]

        current_level[self.strip_quotes(args[-2])] = args[-1]
        return Block(result)

    def body(self, args: List) -> Module:
        args = strip_new_line_tokens(args)
        result: Dict[str, Any] = {}
        for arg in args:
            result = arg.merge_to(result)
        return result

    def to_string_dollar(self, value: Any) -> Any:
        if isinstance(
            value,
            (
                GetAttr,
                GetIndex,
                Splat,
                Call,
                Conditional,
                Operation,
                ListExpr,
                DictExpr,
                Not,
                Identifier,
            ),
        ):
            return Interpolation(value)
        if isinstance(value, str):
            if value.startswith('"') and value.endswith('"'):
                return str(value)[1:-1]
            return str(value)
        return value

    def identifier(self, value: Any) -> Identifier:
        return Identifier(str(value[0]))

    def index_expr_term(self, args: List) -> GetIndex:
        args = strip_new_line_tokens(args)
        return GetIndex(args[0], args[1])

    def index(self, args: List) -> Any:
        args = strip_new_line_tokens(args)
        return self.strip_quotes(args[0])

    def get_attr_expr_term(self, args: List) -> GetAttr:
        return GetAttr(args[0], args[1])

    def attr_splat_expr_term(self, args: List) -> Splat:
        return Splat(args[0], args[1])

    def attr_splat(self, args: List):
        return args

    def full_splat_expr_term(self, args: List) -> Splat:
        return Splat(args[0], args[1])

    def full_splat(self, args: List):
        return args

    def tuple(self, args: List) -> List:
        args = strip_new_line_tokens(args)
        return [self.to_string_dollar(arg) for arg in args]

    def object_elem(self, args: List) -> Dict:
        key = self.strip_quotes(args[0])
        value = self.to_string_dollar(args[1])
        return {key: value}

    def object(self, args: List) -> Dict:
        args = strip_new_line_tokens(args)
        result: Dict[str, Any] = {}
        for arg in args:
            result.update(arg)
        return result

    def function_call(self, args: List) -> Call:
        args = strip_new_line_tokens(args)
        func_name = str(args[0])
        func_args = args[1] if len(args) > 1 else []
        return Call(func_name, func_args)

    def arguments(self, args: List) -> List:
        return args

    def conditional(self, args: List) -> Conditional:
        args = strip_new_line_tokens(args)
        if len(args) == 1:
            return args[0]
        return Conditional(args[0], args[1], args[2])

    def binary_operator(self, args: List):
        return str(args[0])

    def binary_op(self, args: List):
        args = strip_new_line_tokens(args)
        if len(args) == 1:
            return args[0]
        return Operation(args)

    binary_or_op = binary_op
    binary_or_operator = binary_operator

    binary_and_op = binary_op
    binary_and_operator = binary_operator

    binary_eq_op = binary_op
    binary_eq_operator = binary_operator

    binary_test_op = binary_op
    binary_test_operator = binary_operator

    binary_term_op = binary_op
    binary_term_operator = binary_operator

    binary_factor_op = binary_op
    binary_factor_operator = binary_operator

    def for_intro(self, args: List):
        args = strip_new_line_tokens(args)

        if len(args) == 5:
            return [args[1], args[3]]

        if len(args) == 7:
            return [(args[1], args[3]), args[5]]

        raise ValueError(f"invalid for intro: {args}")

    def for_cond(self, args: List):
        args = strip_new_line_tokens(args)
        return args[-1]

    def for_tuple_expr(self, args: List):
        args = strip_new_line_tokens(args)
        element_id, array = args[1]
        element = args[2]
        condition = args[3] if len(args) > 4 else None
        return ListExpr(element_id, array, element, condition)

    def for_object_expr(self, args: List):
        args = strip_new_line_tokens(args)
        element_id, array = args[1]
        key, value = args[2], args[4]
        condition = args[5] if len(args) > 6 else None
        return DictExpr(element_id, array, key, value, condition)

    def unary_op(self, args: List):
        if args[0] == "-":
            return Operation([0, "-", args[1]])

        if args[0] == "!":
            return Not(args[1])

        raise ValueError(f"invalid operator: {args[0]}")

    def new_line_and_or_comma(self, _: List) -> Discard:
        return Discard()

    def new_line_or_comment(self, _: List) -> Discard:
        return Discard()

    def strip_quotes(self, value: Any) -> Any:
        if isinstance(value, str):
            if value.startswith('"') and value.endswith('"'):
                return str(value)[1:-1]
        return value


GRAMMAR_FILE = os.path.join(dirname(__file__), "hcl2_grammar.lark")
with open(GRAMMAR_FILE) as f:
    hcl2 = Lark(
        f.read(),
        parser="lalr",
        lexer="standard",
        start=[
            "module",
            "eval",
        ],
    )


def loads(source, start="module"):
    if start == "module":
        source = source + "\n"

    tree = hcl2.parse(source, start=start)
    transformer = AstTransformer()
    return transformer.transform(tree)


@singledispatch
def _for_iterable(iterable, id_count=1):
    raise ValueError("invalid iterable type: {iterable}")


@_for_iterable.register(tuple)
@_for_iterable.register(list)
def _(iterable, id_count=1):
    for index, element in enumerate(iterable):
        yield element if id_count == 1 else (index, element)


@_for_iterable.register(dict)
def _(iterable, id_count=1):
    for key, value in iterable.items():
        yield key if id_count == 1 else (key, value)


@_for_iterable.register(set)
def _(iterable, id_count=1):
    for element in iterable:
        yield element if id_count == 1 else (element, element)


@singledispatch
def resolve_deps(value: Any, deps: Set):
    pass


@resolve_deps.register
def _(value: JoinedStr, deps: Set):
    for element in value.elements:
        if not isinstance(element, GetAttr):
            continue
        task_keys = list(element.attr_chain)
        if task_keys and task_keys[0] == "task" and len(task_keys) > 3:
            deps.add(".".join(task_keys[:3]))


@resolve_deps.register
def _(value: list, deps: Set):
    for _value in value:
        resolve_deps(_value, deps)


@resolve_deps.register
def _(value: dict, deps: Set):
    for _value in value.values():
        resolve_deps(_value, deps)


@singledispatch
def evaluate(ast, _):
    return ast


@evaluate.register
def _(ast: Module, env):
    return {
        key: evaluate(attribute_or_block, env)
        for key, attribute_or_block in ast.items()
    }


@evaluate.register
def _(ast: Interpolation, env):
    return evaluate(ast.expr, env)


@evaluate.register(GetIndex)
@evaluate.register(GetAttr)
def _(ast: Union[GetIndex, GetAttr], env):
    result = env
    for attr in ast.attr_chain:
        if isinstance(attr, Splat):
            result = evaluate(attr, env)
        elif isinstance(attr, str) and hasattr(result, attr):
            result = getattr(result, attr)
        else:
            try:
                result = result[attr]
            except KeyError as error:
                message = list(ast.attr_chain)
                raise RunflowReferenceError(message) from error
    return result


@evaluate.register
def _(ast: Identifier, env):
    return env[ast]


@evaluate.register
def _(ast: StringLit, _):
    return ast


@evaluate.register
def _(ast: JoinedStr, env):
    result = []
    if len(ast.elements) == 1:
        if isinstance(ast.elements[0], StringLit):
            return str(ast.elements[0])
        return evaluate(ast.elements[0], env)

    for node in ast.elements:
        if isinstance(node, StringLit):
            result.append(str(node))
        else:
            result.append(str(evaluate(node, env)))
    return "".join(result)


@evaluate.register
def _(ast: Not, env):
    return not evaluate(ast.expr, env)


@evaluate.register
def _(ast: Splat, env):
    array = evaluate(ast.array, env)

    def extract(elem, attrs):
        result = elem
        for attr in attrs:
            if isinstance(attr, str) and hasattr(result, attr):
                result = getattr(result, attr)
            else:
                result = result[attr]
        return result

    return [extract(elem, ast.elements) for elem in array]


@evaluate.register
def _(ast: ListExpr, env):
    result = []
    id_count = 2 if isinstance(ast.element_id, tuple) else 1
    for elem in _for_iterable(evaluate(ast.array, env), id_count):
        if id_count == 2:
            index_id, element_id = ast.element_id
            _index, _elem = elem
            newenv = dict(
                env,
                **{
                    str(element_id): _elem,
                    str(index_id): _index,
                },
            )
        else:
            newenv = dict(env, **{str(ast.element_id): elem})
        if ast.condition and not evaluate(ast.condition, newenv):
            continue
        result.append(evaluate(ast.element, newenv))
    return result


@evaluate.register
def _(ast: DictExpr, env):
    result = {}
    id_count = 2 if isinstance(ast.element_id, tuple) else 1
    for elem in _for_iterable(evaluate(ast.array, env), id_count):
        if id_count == 2:
            index_id, element_id = ast.element_id
            _index, _elem = elem
            newenv = dict(
                env,
                **{
                    str(element_id): _elem,
                    str(index_id): _index,
                },
            )
        else:
            newenv = dict(env, **{str(ast.element_id): elem})
        if ast.condition and not evaluate(ast.condition, newenv):
            continue
        key = evaluate(ast.key, newenv)
        value = evaluate(ast.value, newenv)
        result[key] = value
    return result


@evaluate.register
def _(ast: Conditional, env):
    cond = evaluate(ast.predicate, env)

    if cond:
        return evaluate(ast.true_expr, env)

    return evaluate(ast.false_expr, env)


@evaluate.register
def _(ast: Call, env):
    args = evaluate(ast.args, env)
    func_name = str(ast.func_name)
    if ":" in func_name:
        func = import_module(func_name)
    elif func_name in __builtins__:
        func = __builtins__[func_name]
    elif func_name in FUNCS:
        func = FUNCS[func_name]
    elif func_name in env.get("func"):
        func = env["func"][func_name]
    else:
        raise NameError(f"function {ast.func_name} is not defined")
    return func(*args)


OPERATORS = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv,
    "%": operator.mod,
    "<": operator.lt,
    "<=": operator.le,
    ">": operator.gt,
    ">=": operator.ge,
    "==": operator.eq,
    "!=": operator.ne,
}


@evaluate.register
def _(ast: Operation, env):
    result = None
    _operator = None
    for index, elem in enumerate(ast.elements):
        if index == 0:
            result = evaluate(elem, env)
        elif index % 2 == 1:
            _operator = elem
        elif _operator in OPERATORS:
            result = OPERATORS[_operator](result, evaluate(elem, env))
        elif _operator == "||":
            result = result or evaluate(elem, env)
        elif _operator == "&&":
            result = result and evaluate(elem, env)
        else:
            raise ValueError(f"invalid operator: {_operator}")

    return result


@evaluate.register
def _(ast: list, env):
    return [evaluate(a, env) for a in ast]


@evaluate.register
def _(ast: dict, env):
    return {k: evaluate(v, env) for k, v in ast.items()}


FUNCS = {
    "lower": lambda s: s.lower(),
    "upper": lambda s: s.upper(),
    "split": lambda sep, s: s.split(sep),
    "join": lambda sep, s: sep.join(s),
    "tojson": json.dumps,
    "concat": lambda *s: list(itertools.chain(*s)),
    "datetime": datetime,
    "todatetime": parse_datetime,
    "call": lambda obj, meth, args=None, kwargs=None: (
        getattr(obj, meth)(*(args or []), **(kwargs or {}))
    ),
}
