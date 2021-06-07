flow "hello-id-env" {
  task "command" "id" {
    command = "xxd -l $LENGTH -ps /dev/urandom"
    env = {
      LENGTH = "16"
    }
  }
}
