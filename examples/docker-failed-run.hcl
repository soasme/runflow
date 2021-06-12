flow "docker-entrypoint" {
  variable "out" {
    default = ""
  }

  task "docker_run" "exit" {
    image       = "ubuntu:latest"
    command     = "/bin/bash -c 'exit 1'"
  }
}
