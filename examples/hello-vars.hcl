# File: hello_vars.hcl
flow "hello_vars" {
  variable "greeter" {
    default = "world"
  }
  task "bash_run" "echo" {
    command = "echo 'hello ${var.greeter}'"
  }
}
