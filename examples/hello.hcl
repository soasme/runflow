# File: hello.hcl
flow "hello-world" {
  task "bash_run" "echo" {
    command = "echo 'hello world'"
  }
}
