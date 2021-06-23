# File: file_read_from_ftp.hcl
flow "file_read_from_ftp" {

  variable "ftp_host" { default = "" }
  variable "ftp_port" { default = 21 }
  variable "ftp_username" { default = "anon" }
  variable "ftp_password" { default = "" }

  task "file_read" "this" {
    filename = "index.md"

    fs = {
      # Set fs.protocol to "ftp"
      protocol = "ftp"

      # set arguments for ftp connection
      host = var.ftp_host
      port = var.ftp_port

      # set arguments for authentication
      username = var.ftp_username
      password = var.ftp_password

      # set timeout
      timeout = 10
    }
  }

  # Output to the console
  task "file_write" "this" {
    filename = "/dev/stdout"
    content = task.file_read.this.content
  }

}
