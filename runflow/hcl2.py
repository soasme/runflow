"""
This module is a hack for python-hcl2 as it cannot parse hcl2 properly.
See python-hcl2 #6.
"""

from typing import List, Dict, Any

from hcl2.lark_parser import Lark_StandAlone
from hcl2.transformer import DictTransformer as _DictTransformer

class Attribute(dict):

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

class DictTransformer(_DictTransformer):

    def attribute(self, args: List) -> Attribute:
        return Attribute(super().attribute(args))

    def block(self, args: List) -> Block:
        return Block(super().block(args))

    def body(self, args: List) -> Dict[str, List]:
        args = self.strip_new_line_tokens(args)
        result: Dict[str, Any] = {}
        for arg in args:
            result = arg.merge_to(result)
        return result

hcl2 = Lark_StandAlone()

def loads(source, context=None):
    tree = hcl2.parse(source + "\n")
    transformer = DictTransformer(context or {})
    return transformer.transform(tree)
