flow "hello-id" {
  task "command" "id" {
    command = "xxd -l16 -ps /dev/urandom"
  }
}
