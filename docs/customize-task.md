---
sidebar: auto
---

# Develop Your Own Task

It's impossible Runflow can provide all kinds of tasks you need.
When that happens, you can develop your own task and let Runflow
load it before a task run.

You will need to write some Python code and hook it up in a Runflow spec.

## Import Task and Function

The Task class must accept task payload as keyword arguments.

It must has `def run(self, context)` or `async def run(self, context)` method,
which performs the actual task work.

The example below shows how to write something into a file.

<<< @/examples/extensions.py

To load it in the Runflow spec, use `import`.

<<< @/examples/custom_task_type.hcl

::: details Click me to view the run output
Run:

```
$ runflow run custom_task_type.hcl --var out=/tmp/out.txt
[2021-06-13 15:48:35,397] "task.guess_ice_cream.echo" is started.
[2021-06-13 15:48:35,398] "task.guess_ice_cream.echo" is successful.

$ cat /tmp/out.txt
Bingo, it is VANILLA-95
```
:::

Tips:

* The Python code for the task must be in sys.path. Ideally, the code should
  be packaged. Learn how to package a Python project:
  [link](https://packaging.python.org/tutorials/packaging-projects/).

## Register New Task Class

The other approach to register a new task class is through
the `entry_points` facility provided by
[setuptools](https://setuptools.readthedocs.io/en/latest/).

Let's demonstrate it through an example.

Create a new directory for your package:

```bash
$ mkdir /tmp/runflow_vanilla_example
$ cd /tmp/runflow_vanilla_example
```

* Create virtual env.
* Install `build` for building your package.
* Install `runflow`.


```bash
$ python3 -mvenv venv
$ source venv/bin/activate
$ pip install -U build runflow
```

Create some Python files:

```bash
├── src
│   └── runflow_vanilla_example
│       ├── __init__.py
│       └── tasks.py
├── pyproject.toml
└── setup.cfg
```

Implement your Task class in `src/runflow_vanilla_example/tasks.py`:

```python
class GuessIceCreamTask:

    def __init__(self, name, output):
        self.name = name
        self.output = output

    async def run(self, context):
        with open(self.output, 'w') as f:
            f.write(f"Bingo, it is {self.name}")
```

Export it in `src/runflow_vanilla_example/__init__.py`:

```python
from .tasks import GuessIceCreamTask
```

Create a new file `setup.cfg` as required by setuptools:

* Define the metadata for the package.
* Define how to find the package source. In this example, we tell setuptool to find
  the package source in the directory `src/` and include all `runflow_vanilla_example` source.

```toml
[metadata]
name = runflow_vanilla_example
version = 0.1.0
author = Anybody
author_email = anybody@example.org
description = An example package that demonstrates how to register a new task type to Runflow

[options]
package_dir =
    = src
packages = find:

[options.packages.find]
where = src
include =
    runflow_vanilla_example
    runflow_vanilla_example.*

[options.entry_points]
    runflow.tasks =
        guess_ice_cream = runflow_vanilla_example:GuessIceCreamTask
```

If you look a close look at the last section, it means you register a new task type `guess_ice_cream` which
is implemented by the class `GuessIceCreamTask` in package `runflow_vanilla_example`.

Create a new file `pyproject.toml`:

```toml
[build-system]
requires = [
    "setuptools>=42",
    "wheel"
]
build-backend = "setuptools.build_meta"
```

All source are prepared. Let's build:

```bash
$ python -mbuild
...
adding 'runflow_vanilla_example/__init__.py'
adding 'runflow_vanilla_example/tasks.py'
adding 'runflow_vanilla_example-0.1.0.dist-info/METADATA'
adding 'runflow_vanilla_example-0.1.0.dist-info/WHEEL'
adding 'runflow_vanilla_example-0.1.0.dist-info/entry_points.txt'
adding 'runflow_vanilla_example-0.1.0.dist-info/top_level.txt'
adding 'runflow_vanilla_example-0.1.0.dist-info/RECORD'
removing build/bdist.macosx-10.15-x86_64/wheel

$ ls dist/
runflow_vanilla_example-0.1.0.tar.gz
runflow_vanilla_example-0.1.0-py3-none-any.whl
```

In the directory `dist/`, two new package files are created.

We can now install the package file to the env (or actually to the env of your project):

```bash
$ python -mpip install runflow_vanilla_example-0.1.0-py3-none-any.whl
```

After `runflow_vanilla_example` gets installed, Runflow is able to automatically
pick it up and recognize `vanilla_run` as a valid task type.

Hooray!! 🎉

<<< @/examples/use_package.hcl

::: details Click me to view the run output

Run:
```bash
$ runflow run use_package.hcl --var out=/tmp/out.txt
[2021-06-24 23:02:05,109] "task.guess_ice_cream.echo" is started.
[2021-06-24 23:02:05,111] "task.guess_ice_cream.echo" is successful.

$ cat /tmp/out.txt
Bingo, it is VANILLA
```
:::

## Request to Include Your Implementation

Alternatively, you can issue a new PR to Runflow GitHub repo and
request to be included in `runflow.registry:task_implementations`.

## Which Approach Should I Use?

1. If you're experimenting something and have `.hcl` and `.py` files
   in one project, just use `import` block.

2. If you have pretty solid task implementations and have some tests,
   docs, consider package all of them and publish to PyPI.
   This is the most recommended approach.

3. If you think your implementation is very fundamental and deserved
   to reside in `runflow` core library, just send out a PR and let's
   review if it works!
