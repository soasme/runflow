# Quickstart

Assume you have followed [Installation](installation.md) to set your project up and
installed Runflow.

## A Minimal Flow

A minimal flow looks something like this:

```hcl2
# File: hello.rf
flow "hello-world" {
  task "command" "echo" {
    command = "echo 'hello world'"
  }
}
```

Save it as `hello.rf` or something similar.

Let's break down the code.

1. First we define a `flow` block with the name `"hello-world"`.
2. Next we define a task with the run type `"command"` and the name `"echo"`.
3. We then let the task `"echo"` do the actual work: `echo 'hello world'`.

To run the flow, use the `runflow` command or `python3 -m runflow`.

```bash
$ runflow run hello.rf
[2021-06-06 11:51:04,151] Task "echo" is started.
hello world
[2021-06-06 11:51:04,158] Task "echo" is successful.
```

## Flow Variables

The flow can accept some dynamic variables:

```hcl2
# File: hello-vars.rf
flow "hello-world" {
  variable "greeter" {
    default = "world"
  }
  task "command" "echo" {
    command = "echo 'hello ${var.greeter}'"
  }
}
```

Save it as `hello-vars.rf` or something similar.

Comparing to `hello.rf`:

1. First we introduced a `variable` block with the name `greeter`.
2. Next we say the variable has a default value `"world"`.
3. We then let the task `"echo"` say hello to the greeter: `echo 'hello ${var.greeter}'`.
   The syntax `${var.REPLACE_THIS_WITH_A_VARIABLE_NAME}` makes sure the content will be
   dynamically interpolated during the task run.

To run the flow with the default variables:

```bash
$ runflow run hello-vars.rf
[2021-06-06 11:58:14,355] Task "echo" is started.
hello world
[2021-06-06 11:58:14,362] Task "echo" is successful.
```

To provide the task run with a different variable, use `--var`:

```bash
$ runflow run hello-vars.rf --var greeter=runflow
[2021-06-06 11:59:23,533] Task "echo" is started.
hello runflow
[2021-06-06 11:59:23,540] Task "echo" is successful.
```
