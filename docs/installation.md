# Installing Runflow

## Python Version

We recommend using the latest version of Python. Runflow supports Python 3.6 and/or newer.

## Installation

To install Runflow, run:

```bash
$ pip install runflow
```

If you want to install Runflow via Pipenv, run:

```bash
$ pipenv install runflow
```

If you want to install Runflow via poetry, run:

```bash
$ poetry add runflow
```

## Dependencies

Runflow package ships with a minimum set of task types. By default, optional dependencies are not installed.

To enable optional dependencies, you can use pip "extras" syntax:

```bash
$ pip install runflow[docker]
```

## Virtual Environment

Using a virtual environment is highly recommended for managing the dependencies of your project.

Virtual environments are independent Python runtimes. A group of Python libraries and binaries
is laid down one for each project. Packages installed for one project will not affect the other
projects.

Python has `venv` module to create virtual environments.

### Create an Environment

Create a project folder and a venv folder within:

```bash
$ mkdir myflow
$ cd myflow
$ python3 -mvenv venv
```

### Activate the Environment

Before you work on your workflows, activate the environment:

```bash
$ source venv/bin/activate
```

### Install Runflow

Within the activated environment, install Runflow:

```bash
$ pip install runflow
```

## Conclusion

Runflow is now installed.

Next:

* [Quick Start](quickstart.md).
