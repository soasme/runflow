import pytest
import docker
import runflow

def test_file_read(capsys):
    runflow.runflow(module='examples.file_read:flow', vars={})
    out, err = capsys.readouterr()
    assert 'setuptools' in out

def test_file_read_failed(capsys):
    runflow.runflow(module='examples.file_read_failed:flow', vars={})
    out, err = capsys.readouterr()
    assert 'FileNotFoundError' in err

def test_github_fs(capsys):
    runflow.runflow(module='examples.file_read_from_github:flow', vars={})
    out, err = capsys.readouterr()
    assert 'build' in out
    assert 'twine' in out
    assert 'pytest' in out

def test_git_fs(capsys):
    runflow.runflow(module='examples.file_read_from_git:flow', vars={})
    out, err = capsys.readouterr()
    assert 'build' in out
