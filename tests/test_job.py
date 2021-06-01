from runflow import runflow

def test_hello_world(capsys):
    runflow("""
flow "hello-world" {
  task "command" "echo" {
    command = ["echo", "hello world"]
  }
}
    """)
    out, err = capsys.readouterr()
    assert out == 'hello world\n'
