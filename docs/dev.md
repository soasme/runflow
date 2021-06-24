---
sidebar: auto
---

# Development

## Build Package

To build the package, run

```
$ python -mbuild
```

## Auto-format

To auto-format the code, run

```
$ make style
```

## Lint

To perform code quality check, run

```
$ make lint
```

## Test

To test the project, run

```
$ make test
```

## Modify Lark Grammar

If the lark grammar file `runflow/hcl2.lark` is modified, please re-generate the parser module:

```
$ make hcl2

$ git add runflow/hcl2.lark
$ git add runflow/hcl2_parser.py
$ git commit -m'hcl2: which part of grammar is change?'
```
