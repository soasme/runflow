# File: hello.hcl
flow "hello-world" {
  task "command" "echo" {
    command = "echo 'hello world'"
  }
}
