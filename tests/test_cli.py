import pytest
from runflow import cli

def test_cli_run_module(tmpdir, capsys):
    cli(['run', 'examples.hello:flow'])
    out, err = capsys.readouterr()
    assert out == 'hello world\n'

def test_cli_print_help(capsys):
    cli([])
    out, err = capsys.readouterr()
    assert 'runflow' in out


def test_cli(tmpdir):
    flow = tmpdir / "test.hcl"
    out = tmpdir / "out.txt"
    flow.write("""
flow "hello-world" {
  task "bash_run" "echo" {
    command = "echo hello world > ${var.out}"
  }
}
    """)

    cli(['run', '--var', f'out={out}', str(flow)])

    assert out.read() == 'hello world\n'

def test_invalid_cli_option(tmpdir):
    flow = tmpdir / "test.rf"
    out = tmpdir / "out.txt"
    flow.write("""
flow "hello-world" {
  task "bash_run" "echo" {
    command = "echo hello world > ${var.out}"
  }
}
    """)

    with pytest.raises(SystemExit):
        cli(['run', '--var', f'out-2', str(flow)])

