"""
This module is a hack for python-hcl2 as it cannot parse hcl2 properly.
See python-hcl2 #6.
"""

from typing import List, Dict, Any

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

class FormatedStr(str):

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

    def __init__(self, subscripted, slice):
        self.subscripted = subscripted
        self.slice = slice
        self.value = '%s[%s]' % (self.subscripted, self.slice)

    def __str__(self):
        return self.value

    def __repr__(self):
        return self.value

    def __eq__(self, o):
        return (
            isinstance(o, GetIndex)
            and self.subscripted == o.subscripted
            and self.slice == o.slice
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

    def body(self, args: List) -> Dict[str, List]:
        args = self.strip_new_line_tokens(args)
        result: Dict[str, Any] = {}
        for arg in args:
            result = arg.merge_to(result)
        return Module(result)

    def to_string_dollar(self, value: Any) -> Any:
        if isinstance(value, str):
            if value.startswith('"') and value.endswith('"'):
                return str(value)[1:-1]
            return FormatedStr(value)
        return value

    def identifier(self, value: Any) -> Identifier:
        return Identifier(str(value[0]))

    def index_expr_term(self, args: List) -> str:
        args = self.strip_new_line_tokens(args)
        return GetIndex(args[0], args[1])

    def index(self, args: List) -> str:
        args = self.strip_new_line_tokens(args)
        return self.strip_quotes(args[0])


hcl2 = Lark_StandAlone()

def loads(source):
    tree = hcl2.parse(source + "\n")
    transformer = DictTransformer()
    return transformer.transform(tree)
