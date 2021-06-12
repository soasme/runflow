# File: docker-failed-run.hcl
flow "docker-failed-run" {
  task "docker_run" "exit" {
    image       = "ubuntu:latest"
    command     = "/bin/bash -c 'exit 1'"
  }
}
