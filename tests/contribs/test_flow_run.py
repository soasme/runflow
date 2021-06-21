import pytest
import runflow

def test_flow_run_by_path(tmpdir, capsys):
    subflow = tmpdir / "subflow.hcl"
    flow = tmpdir / "test.hcl"

    with open('./examples/flow_example.hcl') as f:
        flow.write(f.read().replace('./examples/hello.hcl', str(subflow)))

    with open('./examples/hello.hcl') as f:
        subflow.write(f.read())

    runflow.runflow(path=flow, vars={})
    out, err = capsys.readouterr()
    assert out == 'hello world\n'

def test_flow_run_by_module(tmpdir, capsys):
    flow = tmpdir / "test.hcl"

    with open('./examples/flow_by_module.hcl') as f:
        flow.write(f.read())

    runflow.runflow(path=flow, vars={})
    out, err = capsys.readouterr()
    assert out == 'hello world\n'

def test_flow_run_by_source(tmpdir, capsys):
    flow = tmpdir / "test.hcl"

    with open('./examples/flow_by_source.hcl') as f:
        flow.write(f.read())

    runflow.runflow(path=flow, vars={})
    out, err = capsys.readouterr()
    assert out == 'hello world\n'

def test_flow_not_exist(tmpdir):
    subflow = tmpdir / "subflow.hcl"
    flow = tmpdir / "test.hcl"

    with open('./examples/flow_example.hcl') as f:
        flow.write(f.read().replace('./examples/hello.hcl', str(subflow)))

    with pytest.raises(OSError):
        runflow.runflow(path=flow, vars={})
