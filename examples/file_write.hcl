# File: file_write.hcl
flow "file_write" {
  task "file_write" "this" {
    filename = "/tmp/file_write.txt"
    content = "foo bar"
  }
}
