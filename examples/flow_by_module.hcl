# File: flow_by_module.hcl
flow "flow_by_module" {
  task "flow_run" "echo" {
    module = "examples.hello:flow"
  }
}
