# File: hello-implicit-deps.hcl
flow "hello-implicit-deps" {
  task "command" "echo" {
    command = "echo 'hello ${task.command.greeter.stdout}'"
  }

  task "command" "greeter" {
    command = "xxd -l16 -ps /dev/urandom"
  }
}