# File: invalid_task_with_same_type_and_name.hcl
# INVALID!

flow "invalid_task_with_same_type_and_name" {
  task "bash_run" "example" {
    command = "echo hello world"
  }

  task "bash_run" "example" {
    command = "echo hello 世界"
  }
}
