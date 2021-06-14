"""
This module is a hack for python-hcl2 as it cannot parse hcl2 properly.
See python-hcl2 #6.

The other reason to customize hcl2 parsing is python-hcl2 DcitTransformer
convert everything on right-hand side to string.

Patch 1: Define an Attribute Field.
Patch 2: `def attribute()`: return an Attribute object.
"""

from typing import List, Dict, Any

from hcl2.lark_parser import Lark_StandAlone
from hcl2.transformer import DictTransformer as _DictTransformer

class Attribute(dict):
    pass

class DictTransformer(_DictTransformer):

    def attribute(self, args: List) -> Attribute:
        return Attribute(super().attribute(args))

    def body(self, args: List) -> Dict[str, List]:
        args = self.strip_new_line_tokens(args)
        result: Dict[str, Any] = {}
        for arg in args:
            if isinstance(arg, Attribute):
                result.update(arg)
                continue
            for key, value in arg.items():
                key = str(key)
                if key not in result:
                    result[key] = [value]
                else:
                    if isinstance(result[key], list):
                        if isinstance(value, list):
                            result[key].extend(value)
                        else:
                            result[key].append(value)
                    else:
                        result[key] = [result[key], value]
        return result

hcl2 = Lark_StandAlone()

def loads(source, context=None):
    tree = hcl2.parse(source + "\n")
    transformer = DictTransformer(context or {})
    return transformer.transform(tree)
