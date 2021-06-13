# Quickstart

Assume you have followed [Installation](installation.md) to set your project up and
installed Runflow.

## A Minimal Flow

A minimal flow looks something like this:

<<< @/examples/hello.hcl

Save it as `hello.hcl` or something similar.

Let's break down the code.

1. First we define a `flow` block with the name `"hello-world"`.
2. Next we define a task with the run type `"command"` and the name `"echo"`.
3. We then let the task `"echo"` do the actual work: `echo 'hello world'`.

To run the flow, use the `runflow` command or `python3 -m runflow`.

```bash
$ runflow run hello.hcl
[2021-06-06 11:51:04,151] Task "echo" is started.
hello world
[2021-06-06 11:51:04,158] Task "echo" is successful.
```

## Flow Variables

The flow can accept some dynamic variables:

<<< @/examples/hello-vars.hcl

Save it as `hello-vars.hcl` or something similar.

Comparing to `hello.hcl`:

1. First we introduced a `variable` block with the name `greeter`.
2. Next we say the variable has a default value `"world"`.
3. We then let the task `"echo"` say hello to the greeter: `echo 'hello ${var.greeter}'`.
   The syntax `${var.REPLACE_THIS_WITH_A_VARIABLE_NAME}` makes sure the content will be
   dynamically interpolated during the task run.

To run the flow with the default variables:

```bash
$ runflow run hello-vars.hcl
[2021-06-13 14:36:10,486] "task.command.echo" is started.
hello world
[2021-06-13 14:36:10,496] "task.command.echo" is successful.
```

To provide the task run with a different variable, use `--var`:

```bash
$ runflow run hello-vars.hcl --var greeter=runflow
[2021-06-13 14:36:27,477] "task.command.echo" is started.
hello runflow2
[2021-06-13 14:36:27,489] "task.command.echo" is successful.
```

Runflow variables can be managed using Environment Variables. The naming convention is `RUNFLOW_VAR_{varname}`.
In this case:

```bash
$ export RUNFLOW_VAR_greeter=runflow
$ runflow run hello-vars.hcl
[2021-06-13 14:35:54,076] "task.command.echo" is started.
hello runflow
[2021-06-13 14:35:54,086] "task.command.echo" is successful.
```

If both Environment Variables and `--var` are provided, `--var` takes precedence.

## Task Dependency

The flow can have multiple tasks, each may depending on another.

<<< @/examples/hello-deps.hcl

Save it as `hello-deps.hcl` or something similar.

Comparing it to `hello-vars.hcl`:

1. First we replace `greeter` to a task with command `xxd -l16 -ps /dev/urandom`. If you're curious what this would do, try it on your console - it will display some random alphabet digits.
2. Next we replace `${var.greeter}` to `${task.command.greeter.stdout}`. It chains the greeter command's stdout to the `echo` command.
3. At last we add a `depends_on` parameter, which explicitly declares the `echo` command depends on `task.command.greeter`. It makes sure `echo` command only run after `greeter` is successfully run.

Let's run it with `runflow run`:

```bash
[2021-06-06 15:31:06,080] Task "greeter" is started.
aff8e7f9b236ef1f436c9f5ce4b9d532
[2021-06-06 15:31:06,090] Task "greeter" is successful.
[2021-06-06 15:31:06,092] Task "echo" is started.
hello aff8e7f9b236ef1f436c9f5ce4b9d532
[2021-06-06 15:31:06,098] Task "echo" is successful.
```

As your can see in the output above, despite of `greeter` being declared beneath `echo` block, it gets executed first.

## Implicit Task Dependency

To make your life easier, Runflow is smart enough to detect the implicit task dependencies if task references are used in other tasks.

For example, `hello-deps.hcl` does not need `depends_on` block at all, because the template variable `${task.command.greeter.stdout}` makes it very clear that task "echo" relies on task "greeter".

<<< @/examples/hello-implicit-deps.hcl

Let's run it with `runflow run`:

```bash
[2021-06-07 16:11:56,782] Task "greeter" is started.
bbd43baa501af05103cdd1ea2e6d9ffa
[2021-06-07 16:11:56,798] Task "greeter" is successful.
[2021-06-07 16:11:56,800] Task "echo" is started.
hello bbd43baa501af05103cdd1ea2e6d9ffa
[2021-06-07 16:11:56,806] Task "echo" is successful.
```

## Concepts

Cool, we have walk through some examples and have first-hand experience on how Runflow is used.

Let's take a break and refresh some concepts.

### Flow

A flow is a series of tasks that are performed in order.

Runflow has a dependency graph of your flow and guarantees the tasks are run when the dependent tasks runs are successful.

### Task

A task is actual work.

In general, each task is performing a logical step in your flow.

### Variable

A variable is a configurable value.

A flow may accept some variables.
