# File: file_read.hcl
flow "file_read" {
  task "file_read" "this" {
    filename = "__nonexist__.toml"
  }
}

