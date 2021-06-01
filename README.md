# Runflow

## What Runflow is?

Runflow is a tool to define and run workflows. To find out more about Flow, check out [runflow.org](https://runflow.org).

Runflow supports Python (3.6, 3.7, 3.8, 3.9). 
The main audiences are data scientists and engineers.

## What Runflow is Not?

Runflow is not for data streaming. Runflow manages computation orchestrations, not data. However, you may constantly trigger Runflow jobs in a mini-batch manner to achieve some kind of streaming.

## Goals

* **Simple**: We want you feel simple when developing and running workflows. No hazzle.
* **Stable**: We want it stable when the data plumbing happens. The failures may happen but the tasks can either be remediated or acknowledged by the maintainers.
* **Flexible**: We want it integrate to many existing solutions to broaden its use cases.

## How You Will Use Runflow?

Runflow provides building blocks for task definitions, workflows, job schedules, failure recovering, command-line interfaces, etc. 

Typically, you will

* Define your workflows in HCL2 syntax.
* Run your workflows using a simple command `runflow run`.

You can choose whatever technology stack you’re familiar with and glue them using Runflow.

(Screenshots)

Alternatives: Airflow, Prefect, Oozie, Azkaban.

## Getting Started

### Setup Python Environment

First, prepare a Python environment:

```
$ python3 -mvenv env
$ source venv/bin/activate
```

Run `pip install runflow` to install the latest version from [PyPI](https://pypi.python.org/pypi/jetflow).

```
$ pip install runflow
```

To install the HEAD, run `pip install git+https://github.com/soasme/runflow.git`.

### Write a Flow Spec

Next, write a flow spec. Let’s create a file "example.rf":

```
$ mkdir myrunflow
$ cd myrunflow
$ vi example.rf
```

```
# Content of example.rf
flow "example" {
  variable "content" {
    default = "Hello World!"
  }
  task "command" "echo" {
    command = ["echo", var.content]
  }
}
```

### Run the Flow

At last, let’s run it.

```
$ runflow run
Hello World!

$ runflow run -var="content=Hello Runflow!"
Hello Runflow!

$ echo 'content = "Hello Runflow!' > input.vars
$ runflow run -var-file="input.vars"
Hello Runflow!

$ runflow run --verbose
[…] Job "example" is started.
[…] Job "example" task "echo" is started.
Hello World!
[…] Job "example" task "echo" is complete.
[…] Job "example" is complete.
```

### What’s Next? 

From this point, you have run a minimal example using Runflow. You can head to the Tutorial section for further examples or the How-to guides section for some common tasks in using and configuring Runflow.

Please read the full [documentation](https://docs.runflow.org/en/stable/) hosted on readthedocs.

## Test

To run all test cases, please run: `pytest tests/`.

## Get in Touch

Please report an issue at: <https://github.com/soasme/runflow>.
