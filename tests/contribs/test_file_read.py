import pytest
import docker
import runflow

def test_file_read(tmpdir, capsys):
    flow = tmpdir / "test.rf"
    out = tmpdir / "out.txt"
    with open('examples/file_read.hcl') as f:
        flow.write(f.read())
    runflow.runflow(flow, {})

    out, err = capsys.readouterr()
    assert 'setuptools' in out

def test_file_read_failed(tmpdir, capsys):
    flow = tmpdir / "test.rf"
    out = tmpdir / "out.txt"
    with open('examples/file_read_failed.hcl') as f:
        flow.write(f.read())

    runflow.runflow(flow, {})

    out, err = capsys.readouterr()
    assert 'FileNotFoundError' in err
