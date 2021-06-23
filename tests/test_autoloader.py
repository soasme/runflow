import pytest


def test_autoloader():
    import runflow.autoloader
    from examples.template import flow
    assert flow

def test_autoloader_syntax_error():
    import runflow.autoloader
    with pytest.raises(ImportError):
        from examples.bad_flow import flow
