import docker
import pytest

import runflow


def test_file_write(tmpdir, capsys):
    flow = tmpdir / "test.hcl"
    out = tmpdir / "out.txt"
    with open('examples/file_write.hcl') as f:
        flow.write(
            f.read().replace('"/tmp/file_write.txt"', 'var.out')
        )

    runflow.runflow(flow, vars={'out': str(out)})

    assert out.read() == 'foo bar'

def test_file_write_stdout(tmpdir, capsys):
    runflow.runflow(path='examples/file_write_stdout.hcl')
    out, err = capsys.readouterr()
    assert out == '{"web_proxy": {"proxy_host": "127.0.0.1", "proxy_port": 8964}}\n'
