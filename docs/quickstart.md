---
sidebar: auto
---

# Quickstart

Assume you have followed [Installation](installation.md) to set your project up and
installed Runflow.

## A Minimal Flow

A minimal flow looks something like this:

<<< @/examples/hello.hcl

Save it as `hello.hcl` or something similar.

Let's break down the code.

1. First we define a `flow` block with the name `"hello-world"`.
2. Next we define a task with the run type `"bash_run"` and the name `"echo"`.
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
[2021-06-13 14:36:10,486] "task.bash_run.echo" is started.
hello world
[2021-06-13 14:36:10,496] "task.bash_run.echo" is successful.
```

To provide the task run with a different variable, use `--var`:

```bash
$ runflow run hello-vars.hcl --var greeter=runflow
[2021-06-13 14:36:27,477] "task.bash_run.echo" is started.
hello runflow2
[2021-06-13 14:36:27,489] "task.bash_run.echo" is successful.
```

Runflow variables can be managed using Environment Variables. The naming convention is `RUNFLOW_VAR_{varname}`.
In this case:

```bash
$ export RUNFLOW_VAR_greeter=runflow
$ runflow run hello-vars.hcl
[2021-06-13 14:35:54,076] "task.bash_run.echo" is started.
hello runflow
[2021-06-13 14:35:54,086] "task.bash_run.echo" is successful.
```

If both Environment Variables and `--var` are provided, `--var` takes precedence.

## Task Dependency

The flow can have multiple tasks, each may depending on another.

<<< @/examples/hello-deps.hcl

Save it as `hello-deps.hcl` or something similar.

Comparing it to `hello-vars.hcl`:

1. First we replace `greeter` to a task with command `xxd -l16 -ps /dev/urandom`. If you're curious what this would do, try it on your console - it will display some random alphabet digits.
2. Next we replace `${var.greeter}` to `${task.bash_run.greeter.stdout}`. It chains the greeter command's stdout to the `echo` command.
3. At last we add a `_depends_on` parameter, which explicitly declares the `echo` command depends on `task.bash_run.greeter`. It makes sure `echo` command only run after `greeter` is successfully run.

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

:::tip
Any argument starts with an underscore (`_`) is used by Runflow, not by the task.
:::

## Implicit Task Dependency

To make your life easier, Runflow is smart enough to detect the implicit task dependencies if task references are used in other tasks.

For example, `hello-deps.hcl` does not need `_depends_on` block at all, because the template variable `${task.bash_run.greeter.stdout}` makes it very clear that task "echo" relies on task "greeter".

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

## Conditional Trigger

The values in task argument `_depends_on` can be not just task references but also any values that can be tested with bool.

If any of the values in task argument `_depends_on` is falsy, then the task will be canceled.

For example, the flow below only output `pyproject.toml` only when version is greater than or equal to "0.6.0".

<<< @/examples/conditional_trigger.hcl

::: details Click me to view the run output
Run (passed):
```
$ runflow run examples/conditional_trigger.hcl  --var version=0.1.0
[2021-06-28 17:18:14,226] "task.file_read.read" is started.
[2021-06-28 17:18:14,227] "task.file_read.read" is successful.
[2021-06-28 17:18:14,227] "task.file_write.echo" is started.
[build-system]
requires = [
    "setuptools>=42",
    "wheel"
]
build-backend = "setuptools.build_meta"
[2021-06-28 17:18:14,227] "task.file_write.echo" is successful.
```

Run (canceled):
```bash
$ runflow run examples/conditional_trigger.hcl  --var version=0.1.0
[2021-06-28 17:15:58,011] "task.file_read.read" is started.
[2021-06-28 17:15:58,012] "task.file_read.read" is successful.
[2021-06-28 17:15:58,012] "task.file_write.echo" is canceled due to falsy deps.
```
:::

## Retry

A task can have an optional argument `_retry` to control the retry behavior in case of execution failure.

To stop the retry after several attempts or several seconds, use `_retry.stop_after`. The value of `stop_after` is a string in form of `M seconds`, or `N times`, or `M seconds | N times` (either M seconds or N times).

To control the waiting periods between each retry, use `_retry.wait`. The value of `wait` should be like function calls below:

* `wait_fixed(N)`: wait fixed amount of seconds.
* `wait_random(M, N)`: wait random amount of seconds.
* `wait_fixed(N) + wait_random(M, N)`: wait fixed amount of seconds plus some jitter seconds.
* `wait_exponential(M, N, O)`: wait 2 ^ x * N seconds between each retry starting with N seconds, then up to O seconds, then O seconds afterwards.
* `wait_chain([wait_fixed(N), wait_random(M, N), ...])`: chain various wait behavior for each retry.

Example usage:

<<< @/examples/retry.hcl

::: details Click me to view the run output
Run:

```bash
$ runflow run examples/retry.hcl
[2021-07-02 11:40:10,640] "task.http_request.this" is started.
[2021-07-02 11:40:22,793] "task.http_request.this" is failed.
... (truncated)
httpx.ConnectError: All connection attempts failed
```
:::

## Timeout

A task can have an optional argument `_timeout` to control the maximum execution time. The task will wait until the execution is actually canceled, so the total wait time may exceed the `_timeout`.

The value should be a number.

Example usage:

<<< @/examples/timeout.hcl

::: details Click me to view the run output
Run:

```bash
$ runflow run examples/timeout.hcl
[2021-07-04 11:18:30,344] "task.http_request.this" is started.
[2021-07-04 11:18:30,404] "task.http_request.this" is failed.
... (truncated)
asyncio.exceptions.TimeoutError
```
:::

Some task types support fine tuning timeouts.
For example, `http_request` can set argument `timeout` to a map.
For those task types don't have timeout arguments, the generic `_timeout` should be used.

## Import Another Flow

If you want to use a flow as part of a new flow, the best way is to import it.

Say we have a flow `examples/template.hcl`:

::: details Click me to view the flow `examples/template.hcl`
<<< @/examples/template.hcl
:::

Now, we can import it using `import.tasks`. The import string for the `.hcl` file should be a valid Python import string ending with `:flow`. The key for the import string will be the task type.

For example, the flow below registers `examples.template:flow` as task type `custom_flow_run`. The payloads of the task body becomes the variables for the reused flow:

<<< @/examples/flow_as_task.hcl

::: details Click me to view the output
```bash
[2021-07-04 15:57:24,513] "task.custom_flow_run.this" is started.
[2021-07-04 15:57:24,513] "task.hcl2_template.this" is started.
[2021-07-04 15:57:24,513] "task.hcl2_template.this" is successful.
[2021-07-04 15:57:24,514] "task.file_write.this" is started.
42
42
42
42
42
[2021-07-04 15:57:24,517] "task.file_write.this" is successful.
[2021-07-04 15:57:24,517] "task.custom_flow_run.this" is successful.
```
:::

## Next to Read

* [Concepts](concepts.md)
