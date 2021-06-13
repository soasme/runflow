# File: file_read.hcl
flow "file_read" {
  task "file_read" "this" {
    filename = "pyproject.toml"
  }
  task "bash_run" "this" {
    command = "echo '${task.file_read.this.content | tojson}'"
  }
}
