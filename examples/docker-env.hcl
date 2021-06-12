# File: docker-env.hcl
flow "docker-env" {
  variable "out" {
    default = ""
  }

  task "docker_run" "echo" {
    image   = "ubuntu:latest"
    command = "env"
    environment = {
      "greeter": "world"
    }
  }

  task "command" "save" {
    command = "echo '${task.docker_run.echo.stdout}' > ${var.out}"
  }
}

