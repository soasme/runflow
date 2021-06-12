flow "docker-entrypoint" {
  variable "out" {
    default = ""
  }

  task "docker_run" "setup" {
    image       = "ubuntu:latest"
    entrypoint  = ["/bin/echo"]
    command     = "runflow is awesome"
  }

  task "command" "save" {
    command = "echo '${task.docker_run.setup.stdout}' > ${var.out}"
  }
}
