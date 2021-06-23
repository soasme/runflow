---
sidebar: auto
---

# Hcl2 Template Task

Hcl2 Template task enables rendering source with given context.

Added in v0.3.0.

## Example Usage

<<< @/examples/template.hcl

::: details Click me to view the run output
Run:

```bash
$ runflow run examples/template.hcl --var global=42
[2021-06-12 20:19:34,003] "task.template.this" is started.
[2021-06-12 20:19:34,003] "task.template.this" is successful.
[2021-06-12 20:19:34,017] "task.file_write.this" is started.
42
42
42
42
42
[2021-06-12 20:19:34,022] "task.file_write.this" is successful.
```
:::

## Argument Reference

The following arguments are supported:

* `source` - (Required, str) The template string.
* `context` - (Optional, map) The context for rendering the template. The context will be merged with global execution context so you are free to use something like `${task.bash_run.TASK_NAME.stdout}` in the source.

## Attributes Reference

The following attributes are supported:

* `content` - The rendered content.
