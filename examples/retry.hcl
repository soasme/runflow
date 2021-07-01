flow "retry" {
  task "http_request" "this" {
    method = "GET"
    url = "http://localhost:8000"
    _retry = {
      stop_after = "10 seconds"
      wait = wait_fixed(3)
    }
  }
}
