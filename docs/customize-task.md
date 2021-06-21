# Develop Your Own Task

It's impossible Runflow can provide all kinds of tasks you need.
When that happens, you can develop your own task and let Runflow
load it before a task run.

You will need to write some Python code and hook it up in a Runflow spec.

## Example Usage

You class name must end with `Task`.

The Task class has a constructor `__init__` method, which accepts the
task payload.

It has `def run(self, context)` or `async def run(self, context)` method,
which performs the actual task work.

<<< @/examples/extensions.py

To load it in the Runflow spec, use `import`:

<<< @/examples/custom_task_type.hcl

Run:

```
$ runflow run custom_task_type.hcl --var out=/tmp/out.txt
[2021-06-13 15:48:35,397] "task.guess_ice_cream.echo" is started.
[2021-06-13 15:48:35,398] "task.guess_ice_cream.echo" is successful.

$ cat /tmp/out.txt
Bingo, it is VANILLA-95
```

Tips:

* The Python code for the task must be in sys.path. Ideally, the code should
  be packaged. Learn how to package a Python project:
  [link](https://packaging.python.org/tutorials/packaging-projects/).
