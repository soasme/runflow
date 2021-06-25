import pytest

import runflow


def test_flow_run_by_path(tmpdir, capsys):
    runflow.runflow(path='./examples/flow_by_path.hcl', vars={})
    out, err = capsys.readouterr()
    assert out == 'hello world\n'

def test_flow_run_by_module(tmpdir, capsys):
    runflow.runflow(path='./examples/flow_by_module.hcl', vars={})
    out, err = capsys.readouterr()
    assert out == 'hello world\n'

def test_flow_run_by_source(tmpdir, capsys):
    flow = tmpdir / "test.hcl"

    with open('./examples/flow_by_source.hcl') as f:
        runflow.runflow(source=f.read(), vars={})

    out, err = capsys.readouterr()
    assert out == 'hello world\n'

def test_flow_not_exist(tmpdir):
    subflow = tmpdir / "subflow.hcl"
    flow = tmpdir / "test.hcl"

    with open('./examples/flow_by_path.hcl') as f:
        flow.write(f.read().replace('./examples/hello.hcl', str(subflow)))

    with pytest.raises(OSError):
        runflow.runflow(path=flow, vars={})

def test_subflow_vars(tmpdir, capsys):
    runflow.runflow(path='./examples/subflow_vars.hcl', vars={})
    out, err = capsys.readouterr()
    assert out == 'hello 世界\n'


def test_flow_exports(capsys):
    runflow.runflow(path='./examples/flow_exports.hcl', vars={})
    out, err = capsys.readouterr()
    assert out == 'hello world\nhello world\n'
