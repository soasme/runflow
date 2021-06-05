# Quickstart

Assume you have followed [Installation](installation.md) to set your project up and installed Runflow.

## A Minimal Flow

A minimal flow looks something like this:

```hcl2
# File: hello.rf
flow "hello-world" {
  task "command" "echo" {
    command = "echo 'hello world'"
  }
}
```

Let's break down the code.

1. First we define a `flow` block with the name `"hello-world"`.
2. Next we define a task with the run type `"command"` and the name `"echo"`.
3. We then let the task `"echo"` do the actual work: `echo 'hello world'`.

Save it as `hello.rf`as something similar.

To run the flow, use the `runflow` command or `python3 -m runflow`.

```bash
$ runflow run hello.rf
[2021-06-06 11:51:04,151] Task "echo" is started.
hello world
[2021-06-06 11:51:04,158] Task "echo" is successful.
```
