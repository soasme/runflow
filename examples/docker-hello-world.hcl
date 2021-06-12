# File: docker-hello-world.hcl
flow "docker-hello-world" {
  variable "out" {
    default = ""
  }

  task "docker_run" "echo" {
    image   = "ubuntu:latest"
    command = "echo hello world"
  }

  task "file_write" "hello-world" {
    filename = var.out
    content = task.docker_run.echo.stdout
  }
}
