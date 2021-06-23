---
sidebar: auto
---

# Flow Run Task

Flow Run task enables running another Flow spec as a task.

## Example Usage

Assume you have a flow spec already, you can use "flow_run" task to trigger the flow run.

You can set `path` to specify which flow spec to run.

<<< @/examples/flow_by_path.hcl

You can set `module` to specify which flow spec to run.

<<< @/examples/flow_by_module.hcl

If the dependent flow requires variables, you can set `vars`. It's a key-value mapping.

<<< @/examples/subflow_vars.hcl

## Argument Reference

The following arguments are supported:

* `path` - (Optional, str) The path to the `".hcl"` file.
* `module` - (Optional, str) The import module to the `".hcl"` module.
* `source` - (Optional, str) The source of Runflow spec.
* `vars` - (Optional, map) The variables for running a flow.
