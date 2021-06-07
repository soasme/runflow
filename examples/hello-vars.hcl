# File: hello-vars.hcl
flow "hello-vars" {
  variable "greeter" {
    default = "world"
  }
  task "command" "echo" {
    command = "echo 'hello ${var.greeter}'"
  }
}
