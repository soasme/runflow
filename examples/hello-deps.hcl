# File: hello-deps.rf
flow "hello-deps" {
  task "bash_run" "echo" {
    command = "echo 'hello ${task.bash_run.greeter.stdout}'"
    depends_on = [
      task.bash_run.greeter
    ]
  }

  task "bash_run" "greeter" {
    command = "xxd -l16 -ps /dev/urandom"
  }
}

