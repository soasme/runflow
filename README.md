<h1 align="center">
  <img alt="Runflow" src="https://github.com/soasme/runflow/raw/main/docs/.vuepress/public/logo.png">
</h1>

<p align="center">
  <a href="https://github.com/soasme/runflow/releases">
    <img alt="GitHub release (latest by semver)" src="https://img.shields.io/pypi/v/runflow?color=%2360be86&style=for-the-badge">
  </a>
  <a href="LICENSE">
    <img alt="License" src="https://img.shields.io/github/license/soasme/runflow?color=%2360be86&style=for-the-badge">
  </a>
  <a href="https://github.com/soasme/runflow/actions">
    <img alt="Unit Testing Status" src="https://img.shields.io/github/workflow/status/soasme/runflow/Unit%20Testing?color=%2360be86&label=UNIT%20TEST&style=for-the-badge">
  </a>
  <a href="https://github.com/soasme/runflow/graphs/contributors">
    <img alt="GitHub contributors" src="https://img.shields.io/github/contributors-anon/soasme/runflow?color=%2360be86&style=for-the-badge">
  </a> 
  <a href="https://github.com/soasme/runflow/stargazers">
    <img alt="GitHub Repo stars" src="https://img.shields.io/github/stars/soasme/runflow?color=%2360be86&label=github%20stars&style=for-the-badge">
  </a>
  <a href="https://gitter.im/soasme/runflow">
    <img alt="Chat on gitter.im" src="https://img.shields.io/gitter/room/soasme/runflow?color=%2360be86&style=for-the-badge">
  </a>
</p>


## What Runflow is?

Runflow is a tool to define and run workflows. To find out more about Runflow, check out [runflow.org](https://runflow.org).

Runflow supports Python (3.7, 3.8, 3.9). 
The main audiences are devops, data scientists and hackers.

Runflow is in alpha release stage.

## What Runflow is Not?

Runflow is not job scheduler. It does not schedule the job runs for you. However, you can combine Runflow with some existing scheduling solutions to run your job periodically, such as APScheduler, crontab, etc.

Runflow is not a job worker. It does not watch workloads from somewhere such as job queue. When the job run is complete, the program exits. Nonetheless, it's quite easy to integrate Runflow with some existing worker solutions, such as Celery, Python-RQ, etc.

## Goals

* **Simple**: We want you feel simple when developing and running workflows. No hazzle.
* **Flexible**: We want it integrate to many existing solutions to broaden its use cases.

## How You Will Use Runflow?

Runflow provides building blocks for defining tasks and workflows, failure recovering, command-line interfaces, etc. 

Typically, you will

* Define your workflows in HCL2 syntax.
* Run your workflows using a simple command `runflow run`.

You can choose whatever technology stack you???re familiar with and glue them using Runflow.

Alternatives: Airflow, Prefect, Oozie, Azkaban.

## Getting Started

### Setup Python Environment

First, prepare a Python environment:

```bash
$ python3 -mvenv env
$ source venv/bin/activate
```

Run `pip install runflow` to install the latest version from [PyPI](https://pypi.org/project/runflow/).

```bash
$ pip install runflow
```

To install the HEAD, run `pip install git+https://github.com/soasme/runflow.git`.

### Write a Flow Spec

Next, write a flow spec. Let???s create a file "example.hcl":

```bash
$ mkdir myrunflow
$ cd myrunflow
$ vi example.hcl
```

```hcl
# File: example.hcl

flow "example" {
  variable "content" {
    default = "Hello World!"
  }

  task "bash_run" "echo" {
    command = "echo ${var.content}"
  }
}
```

### Run the Flow

At last, let???s run it.

```bash
$ runflow run example.hcl
Hello World!

$ runflow run example.hcl --var="content=Hello Runflow!"
Hello Runflow!
```

### What???s Next? 

From this point, you have run a minimal example using Runflow.

For more information, please head to the full [documentation](https://runflow.org).

## Test

To run all of the test cases, please run: `make lint test`.

## Get in Touch

Please report an issue at: <https://github.com/soasme/runflow/issues>.
