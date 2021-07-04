flow "complex_flow_dependency" {
  variable "echo_content" {
    default = ""
  }

  task "bash_run" "echo" {
    command = "echo ${var.echo_content}"
  }

  task "bash_run" "echo1" {
    command = "echo ${task.bash_run.echo.stdout}"
  }

  task "bash_run" "echo2" {
    command = "echo ${task.bash_run.echo.stdout}"
  }

  task "bash_run" "echo3" {
    command = "echo ${task.bash_run.echo.stdout}"
  }

  task "bash_run" "echo4" {
    command = "echo ${task.bash_run.echo2.stdout}"
  }

  task "bash_run" "echo5" {
    command = "echo ${task.bash_run.echo3.stdout}"
  }

  task "bash_run" "echo6" {
    command = "echo echo6"
    _depends_on = [
      task.bash_run.echo4,
      task.bash_run.echo5,
    ]
  }

  task "bash_run" "echo7" {
    command = "echo echo7"
    _depends_on = [
      task.bash_run.echo1,
      task.bash_run.echo6,
    ]
  }
}
