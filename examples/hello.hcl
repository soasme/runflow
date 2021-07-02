# File: hello.hcl

# Define a flow naming as "hello".
# There can only be only one flow declaration per flow file.
flow "hello" {

  # The task defines what should be done.
  # In this example, we run a bash command `echo`.
  task "bash_run" "echo" {
    command = "echo 'hello world'"
  }

}
