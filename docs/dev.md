---
sidebar: auto
---

# Development

## Build Package

To build the package, run

```bash
$ python -mbuild
```

## Auto-format

To auto-format the code, run

```bash
$ make style
```

## Lint

To perform code quality check, run

```bash
$ make lint
```

## Test

To test the project, run

```bash
$ make test
```

## Type Check

To check the types, run

```bash
$ make type
```

## Make

The default make command is equivalent to `make style type lint test`:

```bash
$ make
```

## Modify Lark Grammar

If the lark grammar file `runflow/hcl2.lark` is modified, please re-generate the parser module:

```bash
$ make hcl2

$ git add runflow/hcl2.lark
$ git add runflow/hcl2_parser.py
$ git commit -m'hcl2: which part of grammar is change?'
```
