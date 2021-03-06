---
sidebar: auto
---

# Papermill Execute Task

This task populates a `.ipynb` file with outputs for each cell.

Added since v0.10.0.

::: tip
This feature requires installing jupyterlab and papermill:
```bash
$ pip install runflow[papermill]
```
:::

## Example Usage

* Set task type to `papermill_execute`.
* Set `input_path`, `output_path` and `parameters`.

<<< @/examples/papermill_example.hcl

::: details Click me to view the run output
Run:
```bash
$ runflow run examples/papermill_example.hcl
[2021-07-12 17:45:01,075] "task.papermill_execute.this" is started.
[2021-07-12 17:45:01,076] Input Notebook:  examples/sysexit0.ipynb
[2021-07-12 17:45:01,076] Output Notebook: /tmp/sysexit0-out.ipynb
Executing:   0%|                    | 0/3 [00:00<?, ?cell/s]
[2021-07-12 17:45:02,494] Executing notebook with kernel: python3
Executing:  67%|█████████████▎      | 2/3 [00:01<00:00,  1.30cell/s]
[2021-07-12 17:45:02,649] "task.papermill_execute.this" is successful.
```
:::

## Arguments Reference

* `input_path` - (Required, str or Path) Path to input notebook.
* `output_path` - (Required, str or Path) Path to save executed notebook
* `parameters` - (Optional, map) Arbitrary keyword arguments to pass to the notebook parameters
* `engine_name` - (Optional, str) Name of execution engine to use
* `request_save_on_cell_execute` - (Optional, bool) Request save notebook after each cell execution
* `autosave_cell_every` - (Optional, int) How often in seconds to save in the middle of long cell executions
* `prepare_only` - (Optional, bool) Flag to determine if execution should occur or not
* `kernel_name` - (Optional, str) Name of kernel to execute the notebook against
* `language` - (Optional, str) Programming language of the notebook
* `progress_bar` - (Optional, bool) Flag for whether or not to show the progress bar.
* `log_output` - (Optional, bool) Flag for whether or not to write notebook output to the configured logger
* `start_timeout` - (Optional, int) Duration in seconds to wait for kernel start-up
* `report_mode` - (Optional, bool) Flag for whether or not to hide input.
* `cwd` - (Optional, str or Path) Working directory to use when executing the notebook
* `engine_config` - (Optional, map) Arbitrary keyword arguments to pass to the notebook engine

## Attributes Reference

* `notebook` - The notebook object.
