# File: docker-hello-world.hcl
flow "docker-hello-world" {
  variable "out" {
    default = ""
  }

  task "docker_run" "echo" {
    image   = "ubuntu:latest"
    command = "echo hello world"
  }

  task "command" "save" {
    command = "echo '${task.docker_run.echo.stdout}' > ${var.out}"
  }
}
