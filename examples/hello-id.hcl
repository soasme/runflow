# File: hello-id.hcl
flow "hello-id" {
  task "bash_run" "id" {
    command = "xxd -l16 -ps /dev/urandom"
  }
}
