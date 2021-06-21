# File: flow_by_source.hcl
flow "flow_by_source" {
  task "flow_run" "echo" {
    source = <<-EOT
      flow "hello_world" {
        task "bash_run" "echo" {
          command = "echo 'hello world'"
        }
      }
    EOT
  }
}
