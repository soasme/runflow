# File: http_get.hcl
flow "http_get" {

  variable "out" { default = "" }

  task "http_request" "this" {
    method = "GET"
    url = "https://api.github.com/repos/soasme/runflow"
    headers = {
      "Accept" = "application/vnd.github.v3+json"
    }
    timeout = 3
  }

  task "file_write" "this" {
    filename = var.out
    content  = task.http_request.this.response.text
  }
}
