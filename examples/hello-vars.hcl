# File: hello_vars.hcl
flow "hello_vars" {
  variable "greeter" {
    default = "world"
    required = true
  }
  task "bash_run" "echo" {
    command = "echo 'hello ${var.greeter}'"
  }
}
