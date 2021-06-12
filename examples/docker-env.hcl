# File: docker-env.hcl
flow "docker-env" {
  variable "out" {
    default = ""
  }

  task "docker_run" "this" {
    image   = "ubuntu:latest"
    command = "env"
    environment = {
      "greeter": "world"
    }
  }

  task "file_write" "this" {
    filename = var.out
    content = task.docker_run.this.stdout
  }
}
