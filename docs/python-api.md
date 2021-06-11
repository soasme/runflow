# Python API

## Run Flow Using `runflow`

Assume you have a Runflow spec file `mypackage/hello.hcl`.

<<< @/examples/hello.hcl

Run this flow:

```python
>>> from runflow import runflow
>>> runflow('mypackage/hello.hcl', vars={})
hello world
```

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

Run this flow:

```python
>>> import asyncio
>>> asyncio.run(flow.run(variables={}))
hello world
```
