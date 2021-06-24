# File: use_package.hcl
flow "use_package" {

  variable "out" {
    default = ""
  }

  task "guess_ice_cream" "echo" {
    name = "${upper("vanilla")}"
    output = var.out
  }

}
