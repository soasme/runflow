from runflow import runflow

def test_papermill(tmpdir, capsys):
    runflow(path='examples/papermill_example.hcl', vars={
        'input_dir': 'examples',
        'output_dir': str(tmpdir),
    })
    assert (tmpdir / 'sysexit0-out.ipynb').read()
