import pytest
import docker
import runflow

def test_file_write(tmpdir, capsys):
    flow = tmpdir / "test.rf"
    out = tmpdir / "out.txt"
    with open('examples/file_write.hcl') as f:
        flow.write(
            f.read().replace('"/tmp/file_write.txt"', 'var.out')
        )

    runflow.runflow(flow, {'out': out})

    assert out.read() == 'foo bar'