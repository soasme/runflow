import json

import docker
import pytest

import runflow


def test_http_get(tmpdir, capsys):
    out = tmpdir / "out.txt"
    runflow.runflow(path="examples/http_get.hcl", vars={'out': str(out)})
    data = json.loads(out.read())
    assert data['name'] == 'runflow'


def test_http_post(tmpdir, capsys):
    out = tmpdir / "out.txt"
    runflow.runflow(path="examples/http_post.hcl", vars={'out': str(out)})
    assert '<h1 align="center">' in out.read()


def test_invalid_http_payload(capsys):
    runflow.runflow(source="""
flow "invalid_http_payload" {
  task "http_request" "this" {
    method = "GET"
    url = 1
  }
}
    """)
    _, err = capsys.readouterr()
    assert "'url' must be <class 'str'>" in err


def test_invalid_http_payload2(capsys):
    runflow.runflow(source="""
flow "invalid_http_payload" {
  task "http_request" "this" {
    method = "FETCH"
    url = "https://github.com"
  }
}
    """)
    _, err = capsys.readouterr()
    assert "'method' must be in" in err
    assert "got 'FETCH'" in err
