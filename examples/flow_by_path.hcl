# File: flow_example
flow "flow_example" {
  task "flow_run" "echo" {
    path = "./examples/hello.hcl"
  }
}
