"""
This module is a hack for python-hcl2 as it cannot parse hcl2 attribute/blocks
properly. See amplify-education/python-hcl2#6.

It cannot parse exp values:

    1e7 => lark.exceptions.UnexpectedToken.

It cannot transform full splat:

    a=b[*].1 => {'a': Tree('full_splat_expr_term', ['b', 1])}
"""

import os
import re
import textwrap
from os.path import dirname
from typing import List, Dict, Any

from lark import Token, Lark, Discard, Transformer

HEREDOC_PATTERN = re.compile(r'<<-?([a-zA-Z][a-zA-Z0-9._-]+)\n((.|\n)*?)\n\s*\1', re.S)

class Module(dict):
    pass

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
        self.expr = expr
        self.value = '${%s}' % expr

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
        self.value = '%s[%s]' % (self.expr, self.index)

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

def extract_attr_chain(v, rs):
    if isinstance(v, GetAttr):
        extract_attr_chain(v.expr, rs)
        rs.append(v.attr)
    elif isinstance(v, GetIndex):
        extract_attr_chain(v.expr, rs)
        rs.append(v.index)
    elif isinstance(v, (str, int, )):
        rs.append(v)
    else:
        raise ValueError(v)

class GetAttr:

    def __init__(self, expr, attr):
        self.expr = expr
        self.attr = attr
        self.value = '%s.%s' % (self.expr, self.attr)

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
        rs = []
        extract_attr_chain(self, rs)
        return rs

class Splat:

    def __init__(self, array, elements):
        self.array = array
        self.elements = elements

    def __repr__(self):
        return '%s.*.%s' % (self.array, '.'.join([str(e) for e in self.elements]))

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
        return '%s(%s)' % (self.func_name, ','.join(str(a) for a in self.args))

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
        return '%s ? %s : %s' % (self.predicate, self.true_expr, self.false_expr)

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
        return '(%s)' % (''.join([str(e) for e in self.elements]))

    def __eq__(self, o):
        return (
            isinstance(o, Operation)
            and self.elements == o.elements
        )

class ListExpr:

    def __init__(self, element_id, array, element, condition):
        self.element_id = element_id
        self.array = array
        self.element = element
        self.condition = condition

    def __repr__(self):
        return '[for %s in %s: %s%s]' % (
            ','.join(self.element_id) if isinstance(self.element_id, tuple) else self.element_id,
            self.array,
            self.element,
            f' if {self.condition}' if self.condition else ''
        )

    def __eq__(self, o):
        return (
            isinstance(o, ListExpr)
            and self.element_id == o.element_id
            and self.array == o.array
            and self.element == o.element
            and self.condition == o.condition
        )

class DictExpr:

    def __init__(self, element_id, array, key, value, condition):
        self.array = array
        self.element_id = element_id
        self.key = key
        self.value = value
        self.condition = condition
    def __repr__(self):
        return '{for %s in %s: %s => %s%s}' % (
            ','.join(self.element_id) if isinstance(self.element_id, tuple) else self.element_id,
            self.array,
            self.key,
            self.value,
            f' if {self.condition}' if self.condition else ''
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
        return '(!%s)' % self.expr
    def __eq__(self, o):
        return isinstance(o, Not) and self.expr == o.expr

class DictTransformer(Transformer):

    def module(self, args: List) -> Dict:
        args = self.strip_new_line_tokens(args)
        return Module(args[0])

    def eval(self, args: List) -> Dict:
        return args[0]

    def float_lit(self, args: List) -> float:
        return float("".join([str(arg) for arg in args]))

    def int_lit(self, args: List) -> int:
        return int("".join([str(arg) for arg in args]))

    def expr_term(self, args: List) -> Any:
        args = self.strip_new_line_tokens(args)
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
        args = self.strip_new_line_tokens(args)
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
        args = self.strip_new_line_tokens(args)
        result: Dict[str, Any] = {}
        for arg in args:
            result = arg.merge_to(result)
        return result

    def to_string_dollar(self, value: Any) -> Any:
        if isinstance(value, str):
            if value.startswith('"') and value.endswith('"'):
                return str(value)[1:-1]
            return Interpolation(value)
        if isinstance(value, (GetAttr, GetIndex, Splat, Call, Conditional, Operation,
                ListExpr, DictExpr, Not, )):
            return Interpolation(value)
        return value

    def identifier(self, value: Any) -> Identifier:
        return Identifier(str(value[0]))

    def index_expr_term(self, args: List) -> GetIndex:
        args = self.strip_new_line_tokens(args)
        return GetIndex(args[0], args[1])

    def index(self, args: List) -> Any:
        args = self.strip_new_line_tokens(args)
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
        return [self.to_string_dollar(arg) for arg in self.strip_new_line_tokens(args)]

    def object_elem(self, args: List) -> Dict:
        key = self.strip_quotes(args[0])
        value = self.to_string_dollar(args[1])
        return {key: value}

    def object(self, args: List) -> Dict:
        args = self.strip_new_line_tokens(args)
        result: Dict[str, Any] = {}
        for arg in args:
            result.update(arg)
        return result

    def function_call(self, args: List) -> Call:
        args = self.strip_new_line_tokens(args)
        func_name = str(args[0])
        func_args = args[1] if len(args) > 1 else []
        return Call(func_name, func_args)

    def arguments(self, args: List) -> List:
        return args

    def conditional(self, args: List) -> Conditional:
        args = self.strip_new_line_tokens(args)
        if len(args) == 1:
            return args[0]
        return Conditional(args[0], args[1], args[2])

    def binary_or_op(self, args: List):
        return self.binary_op(args)

    def binary_or_operator(self, args: List):
        return str(args[0])

    def binary_and_op(self, args: List):
        return self.binary_op(args)

    def binary_and_operator(self, args: List):
        return str(args[0])

    def binary_eq_op(self, args: List):
        return self.binary_op(args)

    def binary_eq_operator(self, args: List):
        return str(args[0])

    def binary_test_op(self, args: List):
        return self.binary_op(args)

    def binary_test_operator(self, args: List):
        return str(args[0])

    def binary_factor_op(self, args: List):
        return self.binary_op(args)

    def binary_factor_operator(self, args: List):
        return str(args[0])

    def binary_term_op(self, args: List):
        return self.binary_op(args)

    def binary_term_operator(self, args: List):
        return str(args[0])

    def binary_op(self, args: List):
        args = self.strip_new_line_tokens(args)
        if len(args) == 1:
            return args[0]
        return Operation(args)

    def for_intro(self, args: List):
        args = self.strip_new_line_tokens(args)
        if len(args) == 5:
            return [args[1], args[3]]
        elif len(args) == 6:
            return [(args[1], args[2]), args[4]]
        else:
            raise ValueError(f'invalid for intro: {args}')

    def for_cond(self, args: List):
        args = self.strip_new_line_tokens(args)
        return args[-1]

    def for_tuple_expr(self, args: List):
        args = self.strip_new_line_tokens(args)
        element_id, array = args[1]
        element = args[2]
        condition = args[3] if len(args) > 4 else None
        return ListExpr(element_id, array, element, condition)

    def for_object_expr(self, args: List):
        args = self.strip_new_line_tokens(args)
        element_id, array = args[1]
        key, value = args[2], args[4]
        condition = args[5] if len(args) > 6 else None
        return DictExpr(element_id, array, key, value, condition)

    def unary_op(self, args: List):
        if args[0] == '-':
            return Operation([0, '-', args[1]])
        elif args[0] == '!':
            return Not(args[1])

    def heredoc_template(self, args: List) -> str:
        match = HEREDOC_PATTERN.match(str(args[0]))
        if not match:
            raise RuntimeError("Invalid Heredoc token: %s" % args[0])
        return match.group(2)

    def heredoc_template_trim(self, args: List) -> str:
        return textwrap.dedent(self.heredoc_template(args))

    def new_line_and_or_comma(self, args: List) -> Discard:
        return Discard()

    def new_line_or_comment(self, args: List) -> Discard:
        return Discard()

    def strip_new_line_tokens(self, args: List) -> List:
        return [arg for arg in args if arg != "\n" and not isinstance(arg, Discard)]

    def strip_quotes(self, value: Any) -> Any:
        if isinstance(value, str):
            if value.startswith('"') and value.endswith('"'):
                return str(value)[1:-1]
        return value



GRAMMAR_FILE = os.path.join(dirname(__file__), 'hcl2_grammar.lark')
with open(GRAMMAR_FILE) as f:
    hcl2 = Lark(
        f.read(),
        parser="lalr",
        lexer="standard",
        start=['module', 'eval', ],
    )

def loads(source, start='module'):
    if start == 'module':
        source = source + '\n'

    tree = hcl2.parse(source, start=start)
    transformer = DictTransformer()
    return transformer.transform(tree)
