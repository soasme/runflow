import os

import pytest
import runflow

def test_one_flow_is_required(tmpdir):
    flow = tmpdir / "test.rf"
    flow.write("# nothing ;(")
    with pytest.raises(AssertionError):
        runflow.runflow(flow)

def test_invalid_spec(tmpdir):
    flow = tmpdir / "test.rf"
    flow.write("""
flow "hello-world" {
    """)

    with pytest.raises(runflow.RunflowSyntaxError):
        runflow.runflow(flow)

def test_multiple_flows_are_disallowed(tmpdir):
    flow = tmpdir / "test.rf"
    flow.write("""
flow "hello-world" { }
flow "hello-world2" { }
    """)

    with pytest.raises(AssertionError):
        runflow.runflow(flow)

def test_hello_world(tmpdir):
    flow = tmpdir / "test.rf"
    out = tmpdir / "out.txt"
    flow.write("""
flow "hello-world" {
  task "bash_run" "echo" {
    command = "echo hello world > ${var.out}"
  }
}
    """)

    runflow.runflow(flow, {'out': out})

    assert out.read() == 'hello world\n'

def test_command_env(tmpdir):
    flow = tmpdir / "test.rf"
    out = tmpdir / "out.txt"
    flow.write(r"""
flow "hello-world" {
  task "bash_run" "echo" {
    command = "echo hello $GREETER > ${var.out}"
    env = {
        GREETER = "world"
    }
  }
}
    """)

    runflow.runflow(flow, {'out': out})

    assert out.read() == 'hello world\n'

def test_command_env2(tmpdir):
    flow = tmpdir / "test.rf"
    out = tmpdir / "out.txt"
    flow.write(r"""
flow "hello-world" {
  task "bash_run" "echo" {
    command = "echo hello $GREETER > ${var.out}"
    env = {
        "GREETER" = "world"
    }
  }
}
    """)

    runflow.runflow(flow, {'out': out})

    assert out.read() == 'hello world\n'

def test_command_env3(tmpdir):
    flow = tmpdir / "test.rf"
    out = tmpdir / "out.txt"
    flow.write(r"""
flow "hello-id-env" {
  task "bash_run" "id" {
    command = "xxd -l $LENGTH -ps /dev/urandom > ${var.out}"
    env = {
      LENGTH = 16 # LENGTH value is an integer.
    }
  }
}
    """)

    runflow.runflow(flow, {'out': out})

    assert len(out.read().strip()) == 32

def test_multiple_hello_world(tmpdir):
    flow = tmpdir / "test.rf"
    out1 = tmpdir / "out1.txt"
    out2 = tmpdir / "out2.txt"
    flow.write("""
flow "hello-world" {
  task "bash_run" "out1" {
    command = "echo hello world1 > ${var.out1}"
  }
  task "bash_run" "out2" {
    command = "echo hello world2 > ${var.out2}"
  }
}
    """)

    runflow.runflow(flow, {'out1': out1, 'out2': out2})

    assert out1.read() == 'hello world1\n'
    assert out2.read() == 'hello world2\n'

def test_explicit_depends_on(tmpdir):
    flow = tmpdir / "test.rf"
    out1 = tmpdir / "out1.txt"
    out2 = tmpdir / "out2.txt"
    flow.write("""
flow "hello-world" {
  task "bash_run" "out1" {
    command = "cat ${var.out2} > ${var.out1}"
    depends_on = [task.bash_run.out2]
  }
  task "bash_run" "out2" {
    command = "echo hello world2 > ${var.out2}"
  }
}
    """)

    runflow.runflow(flow, {'out1': out1, 'out2': out2})

    assert out1.read() == 'hello world2\n'
    assert out2.read() == 'hello world2\n'

def test_implicit_depends_on(tmpdir):
    flow = tmpdir / "test.rf"
    out = tmpdir / "out.txt"
    flow.write("""
flow "hello-world" {
  task "bash_run" "out1" {
    command = "echo ${task.bash_run.out2.stdout} > ${var.out}"
  }
  task "bash_run" "out2" {
    command = "echo hello world2"
  }
}
    """)

    runflow.runflow(flow, {'out': out})

    assert out.read() == 'hello world2\n'

def test_depends_on_must_be_a_task(tmpdir):
    flow = tmpdir / "test.rf"
    out1 = tmpdir / "out1.txt"
    out2 = tmpdir / "out2.txt"
    flow.write("""
flow "hello-world" {
  task "bash_run" "out1" {
    command = "cat ${var.out2} > ${var.out1}"
    depends_on = [var.out2]
  }
  task "bash_run" "out2" {
    command = "echo hello world2 > ${var.out2}"
  }
}
    """)

    with pytest.raises(runflow.RunflowSyntaxError):
        runflow.runflow(flow, {'out1': out1, 'out2': out2})

def test_depends_on_must_be_a_reference(tmpdir):
    flow = tmpdir / "test.rf"
    out1 = tmpdir / "out1.txt"
    out2 = tmpdir / "out2.txt"
    flow.write("""
flow "hello-world" {
  task "bash_run" "out1" {
    command = "cat ${var.out2} > ${var.out1}"
    depends_on = ["/path/to/${task.bash_run.out2}"]
  }
  task "bash_run" "out2" {
    command = "echo hello world2 > ${var.out2}"
  }
}
    """)

    with pytest.raises(runflow.RunflowSyntaxError):
        runflow.runflow(flow, {'out1': out1, 'out2': out2})

def test_depends_on_task_type_must_match(tmpdir):
    flow = tmpdir / "test.rf"
    out1 = tmpdir / "out1.txt"
    out2 = tmpdir / "out2.txt"
    flow.write("""
flow "hello-world" {
  task "bash_run" "out1" {
    command = "cat ${var.out2} > ${var.out1}"
    depends_on = ["${task.container.out2}"]
  }
  task "bash_run" "out2" {
    command = "echo hello world2 > ${var.out2}"
  }
}
    """)

    with pytest.raises(runflow.RunflowSyntaxError):
        runflow.runflow(flow, {'out1': out1, 'out2': out2})

def test_unknown_runflow_task_type(tmpdir):
    flow = tmpdir / "test.rf"
    flow.write("""
flow "hello-world" {
  task "___unknown___" "out" {
    command = "echo hello world2"
  }
}
    """)

    with pytest.raises(runflow.RunflowTaskTypeError):
        runflow.runflow(flow)

def test_jinja_replacement(tmpdir):
    flow = tmpdir / "test.rf"
    out = tmpdir / "out.txt"
    flow.write("""
flow "hello-world" {
  task "bash_run" "echo" {
    command = "echo '${var.content}' > ${var.out}"
  }
}
    """)

    runflow.runflow(flow, {'content': 'hello\nworld', 'out': out})
    assert out.read() == 'hello\nworld\n'

def test_invalid_reference_in_command(tmpdir):
    flow = tmpdir / "test.rf"
    out = tmpdir / "out.txt"
    flow.write("""
flow "hello-world" {
  task "bash_run" "echo" {
    command = "echo hello world > ${var.out}"
  }
}
    """)

    with pytest.raises(runflow.RunflowReferenceError):
        runflow.runflow(flow, {'content': 'hello\nworld'})

def test_command_failed(tmpdir, capsys):
    flow = tmpdir / "test.rf"
    out = tmpdir / "out.txt"
    out.write('definitely not hello world')
    flow.write("""
flow "hello-world" {
  variable "out" { default = "" }
  task "bash_run" "echo" {
    command = "/__path__/to/echo hello world && echo hello world > ${var.out}"
  }
}
    """)

    runflow.runflow(flow, {'out': str(out)})
    assert out.read() == 'definitely not hello world'

def test_command_passed_and_then_run_the_next_task(tmpdir, capsys):
    flow = tmpdir / "test.rf"
    out = tmpdir / "out.txt"
    out.write('definitely not hello world')
    flow.write("""
flow "hello-world" {
  variable "out" { default = "" }
  task "bash_run" "echo" {
    command = "echo hello world"
  }
  task "bash_run" "echo2" {
    command = "echo hello world > ${var.out}"
  }
}
    """)

    runflow.runflow(flow, {'out': str(out)})
    assert out.read() == 'hello world\n'

def test_command_failed_canceling_the_next_task(tmpdir, capsys):
    flow = tmpdir / "test.rf"
    out = tmpdir / "out.txt"
    out.write('definitely not hello world')
    flow.write("""
flow "hello-world" {
  variable "out" { default = "" }
  task "bash_run" "echo" {
    command = "/__path__/to/echo hello world"
  }
  task "bash_run" "echo2" {
    command = "echo hello world > ${var.out}"
  }
}
    """)

    runflow.runflow(flow, {'out': str(out)})
    assert out.read() == 'definitely not hello world'

def test_default_variable(tmpdir):
    flow = tmpdir / "test.rf"
    out = tmpdir / "out.txt"
    flow.write("""
flow "hello-world" {
  variable "content" { default = 42 }
  task "bash_run" "echo" {
    command = "echo ${var.content} > ${ var.out }"
  }
}
    """)

    runflow.runflow(flow, {'out': str(out)})

    assert out.read() == '42\n'

def test_acyclic_deps(tmpdir):
    flow = tmpdir / "test.rf"
    out = tmpdir / "out.txt"
    flow.write("""
flow "hello-world" {
  task "bash_run" "echo1" {
    command = "echo ${ task.bash_run.echo2.stdout }"
    depends_on = [task.bash_run.echo2]
  }
  task "bash_run" "echo2" {
    command = "echo ${ task.bash_run.echo1.stdout }"
    depends_on = [task.bash_run.echo1]
  }
}
    """)

    with pytest.raises(runflow.RunflowAcyclicTasksError):
        runflow.runflow(flow, {'out': str(out)})

def test_render_template(tmpdir):
    flow = tmpdir / "test.rf"
    out = tmpdir / "out.txt"
    with open('examples/template.hcl') as f:
        flow.write(f.read())
    runflow.runflow(flow, {'out': str(out)})
    assert out.read() == f'42\n42\n{out}'

def test_default_env(tmpdir, request):
    flow = tmpdir / "test.rf"
    out = tmpdir / "out.txt"

    os.environ['RUNFLOW_VAR_out'] = str(out)
    def clean_env():
        del os.environ['RUNFLOW_VAR_out']
    request.addfinalizer(clean_env)

    flow.write("""
flow "hello-world" {
  variable "out" {}
  task "bash_run" "echo" {
    command = "echo hello world > ${var.out}"
  }
}
    """)

    runflow.runflow(flow, {})

    assert out.read() == 'hello world\n'

def test_load_extension(tmpdir):
    flow = tmpdir / "test.rf"
    out = tmpdir / "out.txt"

    with open('examples/custom_task_type.hcl') as f:
        flow.write(f.read())

    runflow.runflow(flow, {'out': str(out)})

    assert out.read().startswith("Bingo, it is VANILLA-")
