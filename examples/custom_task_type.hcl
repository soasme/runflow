# File: custom_task_type.hcl
flow "custom_task_type" {

  import {
    # `import.tasks` is a map.
    # The map key will become the task type used later.
    # The map value is the import string of task implementation.
    tasks = {
      guess_ice_cream = "examples.extensions:GuessIceCreamTask"
    }

    # `import.functions` is a map.
    # The map key will become the function name used later.
    # The map value is the import string of function.
    functions = {
      randint = "random:randint"
    }
  }

  variable "out" {
    default = ""
  }

  task "guess_ice_cream" "echo" {
    name = "${upper("vanilla")}-${randint(1, 100)}"
    output = var.out
  }

}
