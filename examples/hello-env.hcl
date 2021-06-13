# File: hello-env.hcl
flow "hello-env" {
  task "bash_run" "echo" {
    command = "echo hello $GREETER"
    env = {
        "GREETER" = "world"
    }
  }
}
