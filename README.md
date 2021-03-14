# Jetflow

Jetflow is a Python (3.6, 3.7, 3.8, 3.9) framework for building real-time data pipeline. The main audiences are data scientists and engineers.
It provides building blocks for data schemes, task definitions, workflows, job schedules, visualization, failure recovering, command-line interfaces, etc.

## Goals

* **Simple**: We want you feel simple when developing and running Jetflow pipelines. No hazzle.
* **Stable**: We want it stable when the data plumbing happens. The failures may happen but the tasks can either be remediated or acknowledged by the maintainers 
* **Scalable**: We want Jetflow can schedule and run many tasks.

## Getting Started

Run `pip install jetflow` to install the latest version from [PyPI](https://pypi.python.org/pypi/jetflow).

To install the HEAD, run `pip install git+https://github.com/enqueuezero/jetflow.git`.

## Usage

### One-Off Job

Write a Task: `example.py`:

```python
import time

class TimeTask:
    def run(self):
        print(time.time())
```

Run an one-off job:

```bash
$ jetflow build example:TimeTask
```

### Periodic Job

To run it periodically, add a trigger decorator for the task: `example.py`.

```python
import time
import jetflow

@jetflow.interval('1s')
class TimeTask:
    def run(self):
        print(time.time())
```

Run the scheduler:

```bash
$ jetflow run --module example
```

Want to see more usages? Please read the [documentation](https://jetflow.readthedocs.io/en/stable/) hosted on readthedocs.

## Test

To run all test cases, please run: `pytest tests/`.

## Get in Touch

Please report an issue at: <https://github.com/enqueuezero/metaflow>.
