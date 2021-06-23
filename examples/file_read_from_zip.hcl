# File: file_read_from_zip.hcl
flow "file_read_from_zip" {

  task "file_read" "this" {
    filename = "hello.hcl"

    fs = {
      # Set fs.protocol to "zip"
      protocol = "zip"

      # The file object that contains zip.
      fo = "examples/hello.hcl.zip"
    }
  }

  # Output to the console
  task "file_write" "this" {
    filename = "/dev/stdout"
    content = task.file_read.this.content
  }
}
