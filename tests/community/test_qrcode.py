from runflow import runflow


def test_generate_qrcode(tmpdir):
    with open('examples/qrcode_generate_example.hcl') as f:
        source = f.read().replace('/tmp', str(tmpdir))
    runflow(source=source, vars={})
    out = tmpdir / 'runflow-qrcode.png'
    assert out.read(mode='rb')


def test_generate_qrcode_with_color(tmpdir):
    with open('examples/qrcode_generate_color.hcl') as f:
        source = f.read().replace('/tmp', str(tmpdir))
    runflow(source=source, vars={})
    out = tmpdir / 'runflow-qrcode.png'
    assert out.read(mode='rb')
