from runflow import runflow

def test_hello_world(tmpdir):
    flow = tmpdir / "test.rf"
    out = tmpdir / "out.txt"
    flow.write("""
flow "hello-world" {
  task "command" "echo" {
    command = "echo hello world > ${var.out}"
  }
}
    """)

    runflow(flow, {'out': out})

    assert out.read() == 'hello world\n'

def test_multiple_hello_world(tmpdir):
    flow = tmpdir / "test.rf"
    out1 = tmpdir / "out1.txt"
    out2 = tmpdir / "out2.txt"
    flow.write("""
flow "hello-world" {
  task "command" "out1" {
    command = "echo hello world1 > ${var.out1}"
  }
  task "command" "out2" {
    command = "echo hello world2 > ${var.out2}"
  }
}
    """)

    runflow(flow, {'out1': out1, 'out2': out2})

    assert out1.read() == 'hello world1\n'
    assert out2.read() == 'hello world2\n'

def test_explicit_depends_on(tmpdir):
    flow = tmpdir / "test.rf"
    out1 = tmpdir / "out1.txt"
    out2 = tmpdir / "out2.txt"
    flow.write("""
flow "hello-world" {
  task "command" "out1" {
    command = "cat ${var.out2} > ${var.out1}"
    depends_on = [task.command.out2]
  }
  task "command" "out2" {
    command = "echo hello world2 > ${var.out2}"
  }
}
    """)

    runflow(flow, {'out1': out1, 'out2': out2})

    assert out1.read() == 'hello world2\n'
    assert out2.read() == 'hello world2\n'
