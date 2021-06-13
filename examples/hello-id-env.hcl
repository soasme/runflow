# File: hello-id-env.hcl
flow "hello-id-env" {
  task "bash_run" "id" {
    command = "xxd -l $LENGTH -ps /dev/urandom"
    env = {
      LENGTH = "16"
    }
  }
}
