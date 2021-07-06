---
sidebar: auto
---

# Concepts

## Flow

### What is Flow?

A flow is a network of tasks that can run concurrently or in order.

### What does Flow Look Like?

In Runflow, the flow is written in [HCL2](https://github.com/hashicorp/hcl) syntax and follows the [Flow Spec](flow-spec.md).

Here is a basic example Flow:

![complex_flow_dependency_visualize](/images/complex_flow_dependency_visualize.svg)

::: details Click me to view the flow definition
<<< @/examples/complex_flow_dependency.hcl
:::

It defines 8 tasks. All of them are connected with arrowed lines, indicating the downstream task will be executed only after all of the upstream tasks are successful. For example,

* `task.bash_run.echo1` will be executed only after `task.bash_run.echo` is successful.
* `task.bash_run.echo7` won't be executed if `task.bash_run.echo1` is unsuccessful.

### What is Flow for?

In Runflow, task and flow are two separate of concerns.
The flow does not care how the tasks are actually executed.

Instead, it manages

* The import of tasks and functions from Python interpreter.
* The order of task executions, e.g, which task gets executed first, and which task gets executed afterward.
* The control flow of task executions, e.g, whether to execute a task based on previous task executions.
* Retry the task executions if they fails.
* Abort the task executions if they timeout.
* Some flow-specific metadata, such as documentation, authorship, license, etc.

## Task

### What is Task?

A task is the minimal execution unit and has to be defined within the flow.
Each task in the flow is standalone and shouldn't interfere with each other if implemented properly.

### What does Task Look Like?

In the flow spec, each task has a type, a name, and a body declaring all arguments. The task type is always associated with a Python class having `.run()` method. When the task is executed using Runflow CLI, such a Task is instantiated with arguments declared in the body. You can easily register your own Task implementations by importing it in the flow definition.

For example,

```hcl
task "bash_run" "echo" {
  command = "echo ${var.echo_content}"
}
```

### What is Task for?

In general, each task is performing a logical step in your flow. It is recommended to keep a task as minimal as possible.

Just name a few:

* Read/write a file.
* Run a SQL statement.
* Run a bash command/script.
* Send an HTTP/RPC request.
* Transform DataFrame.
* Fetch a RSS Feed.
* Tweet.
* Publish a Jira comment.
* Send a Slack message.
* Persist `GradientBoostingRegressor()` model to disk in pickle form.
* ... (my fingers are not enough to count now)

## Task Dependency

### What is Task Dependency?

A task can have upstream and downstream dependencies. Usually, you don't need to explicitly declare which task depends on the other - Runflow does that for you as long as the task definition has argument/attribute references from the other tasks. This is done by using HCL2 string interpolation.

### What does Task Dependency Look Like?

In this example, `task.bash_run.echo1` depends on `task.bash_run.echo` because it has an attribute reference `stdout` from `task.bash_run.echo`.

```hcl
task "bash_run" "echo1" {
  command = "echo ${task.bash_run.echo.stdout}"
}
```

### What is Task Dependency For?

The task dependency determines the execution order of a flow.
Upstream tasks always get executed first.
Downstream tasks always get executed afterward.
Downstream tasks will be canceled if any execution of the upstream tasks is unsuccessful.

## Variable

### What is Variable?

A variable is a key-value pair. At runtime, Runflow maintains an environment storing variables and enables variable referencing in later task definitions.

### What does Variable Look Like?

In this example,

* Block `variable "greeter" {}` declares a variable named `greeter`.
* Block `task "bash_run" "echo" {}` has a variable reference `${var.greeter}`, which interpolates the command string dynamically at runtime.

<<< @/examples/hello-vars.hcl

You can overwrite it using Runflow CLI `--var greeter=WORLD`, `--var-file /path/to/vars.hcl` or environment variable `RUNFLOW_VAR_greeter=WORLD`.

### What is Variable For?

If we say a flow is a callable function, then the variables are conceptually function parameters.

## Runflow CLI

### What is Runflow CLI?

Runflow provides a command-line interface for running and inspecting flows.

### What does Runflow CLI Look Like?

* `runflow run` can collect variables from options and environment variables, and then execute all tasks in the right order. When the flow is complete, the program exits.
* `runflow visualize` can draw the tasks and task dependency as a diagram. The output format can be SVG, PNG, DOT, etc. It's useful for understanding the relationship between tasks.

