# File: hello-implicit-deps.hcl
flow "hello-implicit-deps" {
  task "bash_run" "echo" {
    command = "echo 'hello ${task.bash_run.greeter.stdout}'"
  }

  task "bash_run" "greeter" {
    command = "xxd -l16 -ps /dev/urandom"
  }
}
