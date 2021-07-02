---
sidebar: auto
---

# Flow Specification

The Runflow specification, or Runflow spec, defines the schema for
workflows.  The Runflow spec is parsed and executed by Runflow
command-line interface.

Each Runflow spec file has the extension ".hcl" and should has only a
single flow.

## HCL2

In Runflow, one can concisely chain up task executions without loosing
code readability.  Thanks for the
[Hashicorp Configuration Language - HCL](https://github.com/hashicorp/hcl)
language.

The full HCL2 syntax is defined
[here](https://github.com/hashicorp/hcl/blob/main/hclsyntax/spec.md).

All Runflow specs are valid HCL2 files, but not every HCL2 file is valid
Runflow spec.  Based on the HCL2 syntax, we standardize the way how
attributes and blocks are grouped together and make no change to the
semantic of HCL2.

// If you are curious what is HCL1 and why not HCL1, HCL1 is superseded
by more advanced HCL2 and we will not support HCL1 at all.

A minimal Runflow spec looks like this:

<<< @/examples/hello.hcl

The HCL2 syntax consists of only a few basic elements, merely a little
more than [JSON](http://json.org/). Here lists some:

* `Blocks` groups attributes and the other blocks.
  In this example, we have flow block and task block.
* `Attributes` associate a value with a name.
  In this example, `command` is an attribute.
* `Expressions` represent a value, either a constant or referencing
  other values.
  In this example, `"echo 'hello world'"` is an expression of type string.

## Encoding

Runflow spec should be UTF-8 encoded.

## Comments

Runlow spec supports two types of comments:

* `#` followed by any characters until the end of line.
* `//` followed by any characters until the end of line.

We do prefer to use `#`-style comment at all cases for code consistency.

## Identifiers

An identifier is a sequence of alphabets, digits, underscores (`_`) and
hyphens (`-`), with the first character not being a digit. Identifiers
appear in attribute names, block type names, input variables, etc.

## Attributes

An attribute associate a value with a name.

```
command = "echo 'hello world'"
```

The left-hand side of '=' is the attribute name; the right-hand side
of '=' is the attribute value.

To know what attribute name should be used and what kinds of attribute
values should be associated, please refer to the specific block section.

## Blocks

A block groups attributes and the other blocks.

<<< @/examples/hello-env.hcl

A block has a type (`flow` and `task` in this example).
Each block type requires some fixed number of labels (1 for `flow`,
2 for `task` in this example).
Some block type may not require any labels.
All block types must have body enclosed by `{` and `}`.
Inside the block body, there may be zero or more attributes or blocks.

### Flow Block

The flow block is a block with type `flow`. It's the only top-level
block type that Runflow spec supports.

The flow block requires one label as the name for the flow.

Inside the flow block body, available attributes and blocks include:

* Task block.
* Variable block.
* Import block.

### Task Block

The task block is a block with type `task`.

The task block requires two labels, the first one as the type of the task,
the second one as the name of the task. For example,

<<< @/examples/file_read.hcl

The combination of the task type and task name should appear only once.
So this is invalid:

<<< @/examples/invalid_task_with_same_type_and_name.hcl

### Variable Block

The variable block is a block with type `variable`.

The variable block requires one label as the name of the variable.
The Runflow spec allows referencing the value of the variable in
an expression using `var.<NAME>` syntax.

One can provide a default value optionally.

For example,

<<< @/examples/hello-vars.hcl

To provide the task run with non-default variable, use `--var`:

```bash
$ runflow run hello-vars.hcl --var greeter=runflow
[2021-06-13 14:36:27,477] "task.bash_run.echo" is started.
hello runflow2
[2021-06-13 14:36:27,489] "task.bash_run.echo" is successful.
```

### Import Block

The import block is a block with type `import` and requires no labels.

The import block supports two attributes, both requiring a list of modules
to import.

* Attribute `tasks` is an array of import string of Python Task classes.
  The task class should have `async def run(self, context)` method.
  The task class name should end with `Task`.
  A new task type is available after importing the task.
  The task type name is the task class name in camel case split and
  joined by underscores (`_`).
* Attribute `functions` is an array of import string of any Python functions.

The import string is in the form of `path.to.module:target`.

The import block is the main mechanism for the flow to interact with Python
interpreter. You can extend the functionality of Runflow spec by providing
customized task types and functions.

Please read more docs [here](customize-task.md).

## Expressions

Expressions can be simple literal values, such as

* `string`: `"hello"`;
* `number`: `1`, `1.0`;
* `bool`: `true`, `false` (not `True`/`False` like in Python);
* `list` (or `tuple`): `[1, 2, 3]`, `["a", "b"]`;
* `map` (or `object`): `{"key": "value"}`;
* `null`.

Expressions can be a reference. There should be a `variable "command" {}`
block in the Runflow spec and a value for `var.command` provided for
execution.

```
command = var.command
```

Expression can be a function call.
All Python [built-in](https://docs.python.org/3/library/functions.html)
functions can be used, just name a few: `sum()`, `min()`, `max()`,
`hex()`, etc.

More python classes and functions can be imported.
For example, if you have 
[`sh`](https://amoffat.github.io/sh/) installed, you can
set the value for attribute `content` with expression
`ifconfig("lo0")`.

<<< @/examples/sh_example.hcl

Runflow execution engine provides some additional built-in functions,
such as `lower()`, `upper()`, `split()`, etc.

If the final argument is list and followed by `...`, the final argument is expanded as Python star args.

```
str(value, ["utf-8", "strict"]...)

# equivalent to Python `str(value, *["utf-8", "strict"])`
```


If the final argument is dict and followed by `...`, the final argument is expanded as Python double-star kwargs. For example:

```
tojson(value, {indent=2}...)

# equivalent to Python `json.dumps(value, **{"indent": 2})`
```

For a full list of available functions, see the
[function reference](builtin-functions.md).

Expression can also be an string with interpolated expressions.
Inside the interpolated string, you can wrap up another expression
with `${` and `}`. This allows dynamically construct strings from
other values.

```
command = "echo hello ${var.greeter}"
```

You can even have string inside the interpolated string:

```
command = "echo hello ${lower("WORLD")}"
```

Heredoc string expression allows multiple-line string:

```
command = <<EOT
echo 'a
b
c'
EOT
```

If the string literal has nothing but a single interpolated expression,
like `"${ var.greeter }"`, it is equivalent to `var.greeter`.
If you want it as a string anyway, wrap it up using `"${ str(var.greeter) }"`.

Runflow spec supports For expression as well. For example:

```
command = join(" ", concat(["echo"], [for s in var.list : lower(s)]))
```

The value of `var.list` can be any Python iterables, such as tuple,
list, object, set, etc.

For expression can turn into a map:

```
{for s in var.list : s => upper(s)}
```

Runflow spec supports two identifiers in between `for` and `in`,
separated by comma `,`:

* For tuple and list types, the key is the zero-based index into the sequence for each element, and the value is the element value. The elements are visited in index order.
* For object and map types, the key is the string attribute name or element key, and the value is the attribute or element value. The elements are visited in the order defined by a lexicographic sort of the attribute names or keys.
* For set types, the key and value are both the element value. The elements are visited in an undefined but consistent order.

For example:

```
[for k, v in var.map : len(k) + len(v)]
```

Just right before the end character (`]`) of a for expression, an optional
`if condition_expression` is allowed:

```
[for s in var.list : upper(s) if s != ""]
```
