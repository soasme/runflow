# File: file_write_stdout.hcl
flow "file_write_stdout" {
  task "file_write" "this" {
    filename = "/dev/stdout"
    content = tojson({
        web_proxy = {
            proxy_host = "127.0.0.1"
            proxy_port = 8964
        }
    })
  }
}
