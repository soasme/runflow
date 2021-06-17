# File: hello_world.hcl

# This declares a flow as "hello_world".
# There can only be only one flow declaration per flow file.
flow "hello_world" {

  # A task defines what should be done on the host.
  # In this example, we use "task_run" to run an echo command.
  task "bash_run" "echo" {
    command = "echo 'hello world'"
  }

}
