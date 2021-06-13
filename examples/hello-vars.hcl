# File: hello-vars.hcl
flow "hello-vars" {
  variable "greeter" {
    default = "world"
  }
  task "bash_run" "echo" {
    command = "echo 'hello ${var.greeter}'"
  }
}
