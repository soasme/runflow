# File: file_read_b64.hcl
flow "file_read_b64" {
  task "file_read" "this" {
    filename = "pyproject.toml"
  }
  task "bash_run" "this" {
    command = "echo ${task.file_read.this.b64content}"
  }
}

