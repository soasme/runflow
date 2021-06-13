# File: custom-task-type.hcl
flow "custom-task-type" {

  variable "out" {
    default = ""
  }

  task "guess_ice_cream" "echo" {
    name = "vanilla"
    output = var.out
  }

  extensions = [
    "examples.extensions.GuessIceCreamTask"
  ]
}

