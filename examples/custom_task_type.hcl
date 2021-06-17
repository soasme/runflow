# File: custom_task_type.hcl
flow "custom_task_type" {

  import {
    tasks = [
      "examples.extensions:GuessIceCreamTask"
    ]
    functions = [
      "random:randint"
    ]
  }

  variable "out" {
    default = ""
  }

  task "guess_ice_cream" "echo" {
    name = "${upper("vanilla")}-${randint(1, 100)}"
    output = var.out
  }

}

