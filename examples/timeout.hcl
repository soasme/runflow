flow "timeout" {
  task "http_request" "this" {
    method = "GET"
    url = "http://github.com"
    _timeout = 0.01
  }
}
