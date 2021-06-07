# File: hello-env.hcl
flow "hello-env" {
  task "command" "echo" {
    command = "echo hello $GREETER"
    env = {
        "GREETER" = "world"
    }
  }
}
