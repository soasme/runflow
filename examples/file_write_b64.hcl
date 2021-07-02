# File: file_write_b64.hcl
flow "file_write_b64" {
  task "file_write" "this" {
    filename = "/dev/stdout"
    b64content = "aGVsbG8gd29ybGQK"
  }
}

