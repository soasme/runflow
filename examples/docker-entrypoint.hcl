# File: docker-entrypoint.hcl
flow "docker-entrypoint" {
  variable "out" {
    default = ""
  }

  task "docker_run" "this" {
    image       = "ubuntu:latest"
    entrypoint  = ["/bin/echo"]
    command     = "runflow is awesome"
  }

  task "file_write" "this" {
    filename    = var.out
    content     = task.docker_run.this.stdout
  }
}
