import sqlite3
import pytest
import docker
import runflow

def test_sqlite3_row(tmpdir, capsys):
    flow = tmpdir / "test.rf"
    out = tmpdir / "out.db"
    with open('examples/sqlite3_example.hcl') as f:
        flow.write(f.read())
    runflow.runflow(flow, {'db': out})

    out, err = capsys.readouterr()
    assert 'k1: v1' in out


def test_sqlite3_exec(tmpdir, capsys):
    flow = tmpdir / "test.rf"
    out = tmpdir / "out.db"
    with open('examples/sqlite3_exec.hcl') as f:
        flow.write(f.read())
    runflow.runflow(flow, {'db': out})

    with sqlite3.connect(str(out)) as conn:
        cursor = conn.cursor()
        cursor.execute("select * from kvdb")
        rows = list(cursor.fetchall())
        assert rows == [('k1', 'v1'), ('k2', 'v2'), ('k3', 'v3')]
