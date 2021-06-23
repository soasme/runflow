---
sidebar: auto
---

# Python API

## Run Flow Using `runflow`

Assume you have a Runflow spec file `examples/hello.hcl`.

<<< @/examples/hello.hcl

Run this flow:

```python
>>> from runflow import runflow
>>> runflow(path='examples/hello.hcl', vars={})
hello world
```

Another option is through import string:


```python
>>> runflow(module='examples.hello:flow', vars={})
hello world
```

You can also provide it with the source of flow spec:

```python
>>> source = """
... flow "hello_world" {
...   task "bash_run" "echo" {
...     command = "echo 'hello world'"
...   }
... }
... """
>>> runflow(source=source, vars={})
hello world
```

Added in v0.5.0.

## Run Flow Using Autoloader

Assume you have a Runflow spec file `mypackage/hello.hcl`.

<<< @/examples/hello.hcl

Import "runflow.autoloader" and you can import this flow in Python code.

```python
>>> import runflow.autoloader
>>> from mypackage.hello import flow
>>> flow
<runflow.core.Flow object at 0x10ca67f10>
```

Run it by `runflow` function:

```python
>>> runflow(flow=flow, vars={})
```

If you prefer the low-level API, try this:

```python
>>> import asyncio
>>> asyncio.run(flow.run(vars={}))
hello world
```

Added in v0.5.0.
