---
sidebar: auto
---

# Flow Run Task

Flow Run task enables running another Flow spec as a task.

## Example Usage (Path)

Assume you have a flow spec already, you can use "flow_run" task to trigger the flow run.

You can set `path` to specify which flow spec to run.

<<< @/examples/flow_by_path.hcl

::: details Click me to view the run output
Run:

```bash
$ runflow run examples/flow_by_path.hcl
[2021-06-25 11:54:41,276] "task.flow_run.echo" is started.
[2021-06-25 11:54:41,277] "task.bash_run.echo" is started.
hello world
[2021-06-25 11:54:41,289] "task.bash_run.echo" is successful.
[2021-06-25 11:54:41,289] "task.flow_run.echo" is successful.
```
:::

## Example Usage (Module)

You can set `module` to specify which flow spec to run.

<<< @/examples/flow_by_module.hcl

::: details Click me to view the run output
Run:

```bash
$ runflow run examples/flow_by_module.hcl
[2021-06-25 11:55:00,770] "task.flow_run.echo" is started.
[2021-06-25 11:55:00,770] "task.bash_run.echo" is started.
hello world
[2021-06-25 11:55:00,781] "task.bash_run.echo" is successful.
[2021-06-25 11:55:00,781] "task.flow_run.echo" is successful.
```
:::

## Set Flow Variables

If the dependent flow requires variables, you can set `vars`. It's a key-value mapping.

<<< @/examples/subflow_vars.hcl

::: details Click me to view the run output
Run:

```bash
$ runflow run examples/subflow_vars.hcl
[2021-06-25 11:53:28,932] "task.flow_run.this" is started.
[2021-06-25 11:53:28,932] "task.bash_run.echo" is started.
hello 世界
[2021-06-25 11:53:28,944] "task.bash_run.echo" is successful.
[2021-06-25 11:53:28,945] "task.flow_run.this" is successful.
```
:::

## Export Flow Context

You can set an optional argument `exports` to bring the values in the inner
flow run context to the outer flow context.

<<< @/examples/flow_exports.hcl

::: details Click me to view the run output
Run:

```
[2021-06-25 11:43:21,154] "task.flow_run.echo" is started.
[2021-06-25 11:43:21,154] "task.bash_run.echo" is started.
hello world
[2021-06-25 11:43:21,164] "task.bash_run.echo" is successful.
[2021-06-25 11:43:21,165] "task.flow_run.echo" is successful.
[2021-06-25 11:43:21,167] "task.file_write.re-echo" is started.
hello world
[2021-06-25 11:43:21,167] "task.file_write.re-echo" is successful.
```
:::

## Argument Reference

The following arguments are supported:

* `path` - (Optional, str) The path to the `".hcl"` file.
* `module` - (Optional, str) The import module to the `".hcl"` module.
* `source` - (Optional, str) The source of Runflow spec.
* `vars` - (Optional, map) The variables for running a flow.
* `exports` - (Optional, map) The export variables. The key will be used as task attribute name, and the value should be a valid reference in the inner flow run.

## Attributes Reference

The following attributes are supported:

* Any key specified in argument `exports` can be used.
