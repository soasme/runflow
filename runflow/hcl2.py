"""
This module is a hack for python-hcl2 as it cannot parse hcl2 properly.
See python-hcl2 #6.

The other reason to customize hcl2 parsing is python-hcl2 DcitTransformer
convert everything on right-hand side to string.

Patch 1: Define an Attribute Field.
Patch 2: `def attribute()`: return an Attribute object.
"""

import re
import sys
from typing import List, Dict, Any

from lark import Transformer, Discard

HEREDOC_PATTERN = re.compile(r'<<([a-zA-Z][a-zA-Z0-9._-]+)\n((.|\n)*?)\n\s*\1', re.S)
HEREDOC_TRIM_PATTERN = re.compile(r'<<-([a-zA-Z][a-zA-Z0-9._-]+)\n((.|\n)*?)\n\s*\1', re.S)

class Attribute(Dict):
    pass

class Identifier(str):
    pass

class FuncCall:
    def __init__(self, name, args):
        self.name = name
        self.args = args
    def __repr__(self):
        args_str = ','.join([str(a) for a in self.args])
        return f"{self.name}({args_str})"

# pylint: disable=missing-docstring,unused-argument
class FlowTransformer(Transformer):

    def __init__(self, context):
        self.context = context

    def start(self, args: List) -> Dict:
        args = self.strip_new_line_tokens(args)
        return args[0]

    def float_lit(self, args: List) -> float:
        return float("".join([str(arg) for arg in args]))

    def int_lit(self, args: List) -> int:
        return int("".join([str(arg) for arg in args]))

    def expr_term(self, args: List) -> Any:
        args = self.strip_new_line_tokens(args)
        return args[1] if args[0] == '(' else args[0]

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

    def new_line_and_or_comma(self, args: List) -> Discard:
        return Discard()

    def block(self, args: List) -> Dict:
        args = self.strip_new_line_tokens(args)

        # if the last token is a string instead of an object then the block is empty
        # such as 'foo "bar" "baz" {}'
        # in that case append an empty object
        if isinstance(args[-1], str):
            args.append({})

        result: Dict[str, Any] = {}
        current_level = result
        for arg in args[0:-2]:
            current_level[self.strip_quotes(arg)] = {}
            current_level = current_level[self.strip_quotes(arg)]

        current_level[self.strip_quotes(args[-2])] = args[-1]

        return result

    def attribute(self, args: List) -> Dict:
        key = str(args[0])
        if key.startswith('"') and key.endswith('"'):
            key = key[1:-1]
        value = self.to_string_dollar(args[1])

        # RUNFLOW PATCH: return Attribute instead of dict.
        return Attribute({
            key: value
        })

    def function_call(self, args: List) -> str:
        args = self.strip_new_line_tokens(args)
        return FuncCall(str(args[0]), args[1])

    ####

    def index_expr_term(self, args: List) -> str:
        args = self.strip_new_line_tokens(args)
        return "%s%s" % (str(args[0]), str(args[1]))

    def index(self, args: List) -> str:
        args = self.strip_new_line_tokens(args)
        return "[%s]" % (str(args[0]))

    def get_attr_expr_term(self, args: List) -> str:
        return "%s.%s" % (str(args[0]), str(args[1]))

    def attr_splat_expr_term(self, args: List) -> str:
        return "%s.*.%s" % (args[0], args[1])

    def tuple(self, args: List) -> List:
        return [self.to_string_dollar(arg) for arg in self.strip_new_line_tokens(args)]

    def arguments(self, args: List) -> List:
        return args

    def one_line_block(self, args: List) -> Dict:
        return self.block(args)

    def conditional(self, args: List) -> str:
        args = self.strip_new_line_tokens(args)
        return "%s ? %s : %s" % (args[0], args[1], args[2])

    def binary_op(self, args: List) -> str:
        return " ".join([str(arg) for arg in args])

    def unary_op(self, args: List) -> str:
        return "".join([str(arg) for arg in args])

    def binary_term(self, args: List) -> str:
        args = self.strip_new_line_tokens(args)
        return " ".join([str(arg) for arg in args])

    def body(self, args: List) -> Dict[str, List]:
        # A body can have multiple attributes with the same name
        # For example multiple Statement attributes in a IAM resource body
        # So This returns a dict of attribute names to lists
        # The attribute values will always be lists even if they aren't repeated
        # and only contain a single entry
        args = self.strip_new_line_tokens(args)
        result: Dict[str, Any] = {}
        for arg in args:
            # RUNFLOW PATCH: merge arg if it's attribute
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

    def binary_operator(self, args: List) -> str:
        return str(args[0])

    def heredoc_template(self, args: List) -> str:
        match = HEREDOC_PATTERN.match(str(args[0]))
        if not match:
            raise RuntimeError("Invalid Heredoc token: %s" % args[0])
        return '"%s"' % match.group(2)

    def heredoc_template_trim(self, args: List) -> str:
        # See https://github.com/hashicorp/hcl2/blob/master/hcl/hclsyntax/spec.md#template-expressions
        # This is a special version of heredocs that are declared with "<<-"
        # This will calculate the minimum number of leading spaces in each line of a heredoc
        # and then remove that number of spaces from each line
        match = HEREDOC_TRIM_PATTERN.match(str(args[0]))
        if not match:
            raise RuntimeError("Invalid Heredoc token: %s" % args[0])

        text = match.group(2)
        lines = text.split('\n')

        # calculate the min number of leading spaces in each line
        min_spaces = sys.maxsize
        for line in lines:
            leading_spaces = len(line) - len(line.lstrip(' '))
            min_spaces = min(min_spaces, leading_spaces)

        # trim off that number of leading spaces from each line
        lines = [line[min_spaces:] for line in lines]

        return '"%s"' % '\n'.join(lines)

    def new_line_or_comment(self, args: List) -> Discard:
        return Discard()

    def for_tuple_expr(self, args: List) -> str:
        args = self.strip_new_line_tokens(args)
        for_expr = " ".join([str(arg) for arg in args[1:-1]])
        return '[%s]' % for_expr

    def for_intro(self, args: List) -> str:
        args = self.strip_new_line_tokens(args)
        return " ".join([str(arg) for arg in args])

    def for_cond(self, args: List) -> str:
        args = self.strip_new_line_tokens(args)
        return " ".join([str(arg) for arg in args])

    def for_object_expr(self, args: List) -> str:
        args = self.strip_new_line_tokens(args)
        for_expr = " ".join([str(arg) for arg in args[1:-1]])
        return '{%s}' % for_expr

    def strip_new_line_tokens(self, args: List) -> List:
        """
        Remove new line and Discard tokens.
        The parser will sometimes include these in the tree so we need to strip them out here
        """
        return [arg for arg in args if arg != "\n" and not isinstance(arg, Discard)]

    def to_string_dollar(self, value: Any) -> Any:
        """Wrap a string in ${ and }"""
        if isinstance(value, str):
            if value.startswith('"') and value.endswith('"'):
                return str(value)[1:-1]
            return '${%s}' % value
        return value

    def strip_quotes(self, value: Any) -> Any:
        """Remove quote characters from the start and end of a string"""
        if isinstance(value, str):
            if value.startswith('"') and value.endswith('"'):
                return str(value)[1:-1]
        return value

    def identifier(self, value: Any) -> Any:
        # Making identifier a token by capitalizing it to IDENTIFIER
        # seems to return a token object instead of the str
        # So treat it like a regular rule
        # In this case we just convert the whole thing to a string
        if value[0] == "true":
            return True

        if value[0] == "false":
            return False

        if value[0] == "null":
            return None

        return Identifier(value[0])


from hcl2.lark_parser import Lark_StandAlone

hcl2 = Lark_StandAlone()

def loads(source, context=None):
    tree = hcl2.parse(source + "\n")
    transformer = FlowTransformer(context or {})
    return transformer.transform(tree)
