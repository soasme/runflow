# File: hello-deps.rf
flow "hello-deps" {
  task "command" "echo" {
    command = "echo 'hello ${task.command.greeter.stdout}'"
    depends_on = [
      task.command.greeter
    ]
  }

  task "command" "greeter" {
    command = "xxd -l16 -ps /dev/urandom"
  }
}

