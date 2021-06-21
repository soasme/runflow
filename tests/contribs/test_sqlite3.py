import sqlite3
import pytest
import docker
import runflow


def test_sqlite3_exec(tmpdir, capsys):
    flow = tmpdir / "test.hcl"
    out = tmpdir / "out.db"
    with open('examples/sqlite3_exec.hcl') as f:
        flow.write(f.read())
    runflow.runflow(flow, vars={'db': f"sqlite:///{out}"})

    with sqlite3.connect(str(out)) as conn:
        cursor = conn.cursor()
        cursor.execute("select * from kvdb")
        rows = list(cursor.fetchall())
        assert rows == [('k1', 'v1'), ('k2', 'v2'), ('k3', 'v3')]

def test_sqlite3_row(tmpdir, capsys):
    flow = tmpdir / "test.hcl"
    out = tmpdir / "out.db"

    with open('examples/sqlite3_exec.hcl') as f:
        flow.write(f.read())
    runflow.runflow(flow, vars={'db': f"sqlite:///{out}"})

    with open('examples/sqlite3_row.hcl') as f:
        flow.write(f.read())
    runflow.runflow(flow, vars={'db': f"sqlite:///{out}"})

    out, err = capsys.readouterr()
    assert 'k1: v1' in out
    assert 'kall: [["k1", "v1"], ["k2", "v2"], ["k3", "v3"]]' in out
