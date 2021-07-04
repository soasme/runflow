flow "flow_as_task" {

  import {
    tasks = {
      custom_flow_run = "examples.template:flow"
    }
  }

  task "custom_flow_run" "this" {
    global = 42
  }
}
