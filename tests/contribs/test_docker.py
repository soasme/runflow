import pytest
import docker
import runflow

def test_docker_hello_world(tmpdir):
    flow = tmpdir / "test.hcl"
    out = tmpdir / "out.txt"
    with open('examples/docker-hello-world.hcl') as f:
        flow.write(f.read())
    runflow.runflow(flow, vars={'out': out})
    assert out.read() == 'hello world'

def test_docker_env(tmpdir):
    flow = tmpdir / "test.hcl"
    out = tmpdir / "out.txt"
    with open('examples/docker-env.hcl') as f:
        flow.write(f.read())
    runflow.runflow(flow, vars={'out': out})
    assert 'greeter=world' in out.read()

def test_docker_entrypoint(tmpdir):
    flow = tmpdir / "test.hcl"
    out = tmpdir / "out.txt"
    with open('examples/docker-entrypoint.hcl') as f:
        flow.write(f.read())
    runflow.runflow(flow, vars={'out': out})
    assert out.read() == 'runflow is awesome'

def test_docker_container_failed_run(tmpdir, capsys):
    flow = tmpdir / "test.hcl"
    with open('examples/docker-failed-run.hcl') as f:
        flow.write(f.read())
    runflow.runflow(flow, vars={})
    out, err = capsys.readouterr()
    assert 'docker.errors.ContainerError' in err
