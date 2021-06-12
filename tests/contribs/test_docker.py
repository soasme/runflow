import pytest
import runflow

def test_docker_hello_world(tmpdir):
    flow = tmpdir / "test.rf"
    out = tmpdir / "out.txt"
    flow.write("""
flow "docker-hello-world" {
  variable "out" {
    default = ""
  }

  task "docker_run" "echo" {
    image   = "ubuntu:latest"
    command = "echo hello world"
  }

  task "command" "save" {
    command = "echo ${task.docker_run.echo.stdout} > ${var.out}"
  }
}
    """)

    runflow.runflow(flow, {'out': out})

    assert out.read() == 'hello world\n'

def test_docker_env(tmpdir):
    flow = tmpdir / "test.rf"
    out = tmpdir / "out.txt"
    flow.write("""
flow "docker-env" {
  variable "out" {
    default = ""
  }

  task "docker_run" "echo" {
    image   = "ubuntu:latest"
    command = "env"
    environment = {
      "greeter": "world"
    }
  }

  task "command" "save" {
    command = "echo '${task.docker_run.echo.stdout}' > ${var.out}"
  }
}
    """)

    runflow.runflow(flow, {'out': out})

    assert 'greeter=world' in out.read()
