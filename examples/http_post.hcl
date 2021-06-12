# File: http_post.hcl
flow "http_post" {

  variable "out" { default = "" }

  task "file_read" "this" {
    filename = "README.md"
  }

  task "http_request" "this" {
    method = "POST"
    url = "https://api.github.com/markdown"
    headers = {
      "Accept" = "application/vnd.github.v3+json"
    }
    json = {
      "text" = task.file_read.this.content
    }
    timeout = 3
  }

  task "file_write" "this" {
    filename = var.out
    content  = task.http_request.this.response.text
  }
}

