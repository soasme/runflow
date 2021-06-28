flow "conditional_trigger" {

  variable "version" {
    default = "0.6.0"
  }

  task "file_read" "read" {
    filename = "pyproject.toml"
  }

  task "file_write" "echo" {
    filename = "/dev/stdout"
    content = task.file_read.read.content

    _depends_on = [
      var.version >= "0.6.0"
    ]
  }

}
