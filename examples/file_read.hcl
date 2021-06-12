# File: file_read.hcl
flow "file_read" {
  task "file_read" "this" {
    filename = "pyproject.toml"
  }
  task "command" "this" {
    command = "echo '${task.file_read.this.content | tojson}'"
  }
}
