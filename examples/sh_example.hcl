# File: sh_example.hcl
flow "sh_example" {
  import {
    functions = [
      "sh:ifconfig",
    ]
  }
  variable "out" {
    default = "/tmp/out.txt"
  }
  task "file_write" "this" {
    filename = var.out
    content = ifconfig("lo0")
  }
}
