# File: flow_exports
flow "flow_exports" {

  task "flow_run" "echo" {
    path = "./examples/hello.hcl"

    # You can set as many custom fields in `export` block,
    # as long as the values in block are valid variable references
    # in the flow `./examples/hello.hcl`.
    export {

      # In this example, since `task "bash_run" "echo" {...}`
      # has attribute `stdout`, you can export the stdout value
      # and bind it to any field name, like `custom_field`.
      custom_field = "task.bash_run.echo.stdout"
    }
  }

  task "file_write" "re-echo" {
    filename = "/dev/stdout"

    # Now we can use `task.flow_run.echo.custom_field` data.
    content = task.flow_run.echo.custom_field
  }
}
