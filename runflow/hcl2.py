"""
This module is a hack for python-hcl2 as it cannot parse hcl2 attribute/blocks
properly. See amplify-education/python-hcl2#6.

It cannot parse exp values:

    1e7 => lark.exceptions.UnexpectedToken.

It cannot transform full splat:

    a=b[*].1 => {'a': Tree('full_splat_expr_term', ['b', 1])}
"""

from typing import List, Dict, Any

from lark import Token
from hcl2.lark_parser import Lark_StandAlone
from hcl2.transformer import DictTransformer as _DictTransformer

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
        return self.expr == o.expr

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

class DictTransformer(_DictTransformer):

    def attribute(self, args: List) -> Attribute:
        key = str(args[0])
        if key.startswith('"') and key.endswith('"'):
            key = key[1:-1]
        value = self.to_string_dollar(args[1])
        return Attribute(key, value)

    def block(self, args: List) -> Block:
        return Block(super().block(args))

    def body(self, args: List) -> Module:
        args = self.strip_new_line_tokens(args)
        result: Dict[str, Any] = {}
        for arg in args:
            result = arg.merge_to(result)
        return Module(result)

    def to_string_dollar(self, value: Any) -> Any:
        if isinstance(value, str):
            if value.startswith('"') and value.endswith('"'):
                return str(value)[1:-1]
            return Interpolation(value)
        if isinstance(value, (GetAttr, GetIndex, Splat, Call, Conditional, )):
            return Interpolation(value)
        return value

    def identifier(self, value: Any) -> Identifier:
        return Identifier(str(value[0]))

    def index_expr_term(self, args: List) -> GetIndex:
        args = self.strip_new_line_tokens(args)
        return GetIndex(args[0], args[1])

    def index(self, args: List) -> Any:
        args = self.strip_new_line_tokens(args)
        if isinstance(args[0], Token) and args[0].type == 'DECIMAL':
            return int(str(''.join(args)))
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

    def function_call(self, args: List) -> Call:
        args = self.strip_new_line_tokens(args)
        func_name = str(args[0])
        func_args = args[1] if len(args) > 1 else []
        return Call(func_name, func_args)

    def conditional(self, args: List) -> Conditional:
        args = self.strip_new_line_tokens(args)
        return Conditional(args[0], args[1], args[2])


hcl2 = Lark_StandAlone()

def loads(source):
    tree = hcl2.parse(source + "\n")
    transformer = DictTransformer()
    return transformer.transform(tree)
