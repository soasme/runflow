# File: subflow_vars.hcl
flow "subflow_vars" {
  task "flow_run" "this" {
    path = "./examples/hello-vars.hcl"
    vars = {
      greeter = "世界"
    }
  }
}
