import json
import pytest
import docker
import runflow

def test_http_get(tmpdir, capsys):
    flow = tmpdir / "test.hcl"
    out = tmpdir / "out.txt"
    with open('examples/http_get.hcl') as f:
        flow.write(f.read())
    runflow.runflow(flow, vars={'out': out})

    data = json.loads(out.read())

    assert data['name'] == 'runflow'

def test_http_post(tmpdir, capsys):
    flow = tmpdir / "test.hcl"
    out = tmpdir / "out.txt"
    with open('examples/http_post.hcl') as f:
        flow.write(f.read())
    runflow.runflow(flow, vars={'out': out})

    assert '<h1>' in out.read()
