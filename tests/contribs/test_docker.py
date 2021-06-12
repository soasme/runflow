import pytest
import docker
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

def test_docker_entrypoint(tmpdir):
    flow = tmpdir / "test.rf"
    out = tmpdir / "out.txt"
    flow.write("""
flow "docker-entrypoint" {
  variable "out" {
    default = ""
  }

  task "docker_run" "setup" {
    image       = "ubuntu:latest"
    entrypoint  = ["/bin/echo"]
    command     = "runflow is awesome"
  }

  task "command" "save" {
    command = "echo '${task.docker_run.setup.stdout}' > ${var.out}"
  }
}
    """)

    runflow.runflow(flow, {'out': out})

    assert out.read() == 'runflow is awesome\n'

def test_docker_container_failed_run(tmpdir, capsys):
    flow = tmpdir / "test.rf"
    flow.write("""
flow "docker-entrypoint" {
  variable "out" {
    default = ""
  }

  task "docker_run" "exit" {
    image       = "ubuntu:latest"
    command     = "/bin/bash -c 'exit 1'"
  }
}
    """)

    runflow.runflow(flow, {})
    out, err = capsys.readouterr()
    assert 'docker.errors.ContainerError' in err
