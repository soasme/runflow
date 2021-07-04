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
[2021-07-04 17:01:58,735] "task.flow_run.echo" is started.
[2021-07-04 17:01:58,737] "task.flow_run.echo > task.bash_run.echo" is started.
hello world
[2021-07-04 17:01:58,745] "task.flow_run.echo > task.bash_run.echo" is successful.
[2021-07-04 17:01:58,746] "task.flow_run.echo" is successful.
```
:::

## Example Usage (Module)

You can set `module` to specify which flow spec to run.

<<< @/examples/flow_by_module.hcl

::: details Click me to view the run output
Run:

```bash
$ runflow run examples/flow_by_module.hcl
[2021-07-04 17:02:37,230] "task.flow_run.echo" is started.
[2021-07-04 17:02:37,235] "task.flow_run.echo > task.bash_run.echo" is started.
hello world
[2021-07-04 17:02:37,244] "task.flow_run.echo > task.bash_run.echo" is successful.
[2021-07-04 17:02:37,244] "task.flow_run.echo" is successful.
```
:::

## Set Flow Variables

If the dependent flow requires variables, you can set `vars`. It's a key-value mapping.

<<< @/examples/subflow_vars.hcl

::: details Click me to view the run output
Run:

```bash
$ runflow run examples/subflow_vars.hcl
[2021-07-04 17:02:53,064] "task.flow_run.this" is started.
[2021-07-04 17:02:53,068] "task.flow_run.this > task.bash_run.echo" is started.
hello 世界
[2021-07-04 17:02:53,078] "task.flow_run.this > task.bash_run.echo" is successful.
[2021-07-04 17:02:53,078] "task.flow_run.this" is successful.
```
:::

## Export Flow Context

You can set an optional argument `export` to bring the values in the inner
flow run context to the outer flow context.

<<< @/examples/flow_exports.hcl

::: details Click me to view the run output
Run:

```
$ runflow run examples/flow_exports.hcl
[2021-07-04 17:03:11,601] "task.flow_run.echo" is started.
[2021-07-04 17:03:11,603] "task.flow_run.echo > task.bash_run.echo" is started.
hello world
[2021-07-04 17:03:11,613] "task.flow_run.echo > task.bash_run.echo" is successful.
[2021-07-04 17:03:11,614] "task.flow_run.echo" is successful.
[2021-07-04 17:03:11,614] "task.file_write.re-echo" is started.
hello world
[2021-07-04 17:03:11,617] "task.file_write.re-echo" is successful.
```
:::

## Argument Reference

The following arguments are supported:

* `path` - (Optional, str) The path to the `".hcl"` file.
* `module` - (Optional, str) The import module to the `".hcl"` module.
* `source` - (Optional, str) The source of Runflow spec.
* `vars` - (Optional, map) The variables for running a flow.
* `export` - (Optional, block) The exported variables. The key will be used as task attribute name, and the value should be a valid reference in the inner flow run.

## Attributes Reference

The following attributes are supported:

* Any key specified in argument `exports` can be used.