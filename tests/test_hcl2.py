import pytest

from runflow import hcl2

@pytest.mark.parametrize('input, output', [
    ('a = 1', {'a': 1}),
    ('a = true', {'a': True}),
    ('a = false', {'a': False}),
    ('a = {}', {'a': {}}),
])
def test_attribute(input, output):
    assert hcl2.loads(input) == output

@pytest.mark.parametrize('input, output', [
    ('a {}', {'a': [{}]}),
    ('''
        a {k = 1}
        a {k = 2}
    ''', {'a': [{"k": 1}, {"k": 2}]}),
    ('''
        a {k = 1}
        a = {k = 2}
    ''', {'a': {"k": 2}}),
    ('''
        a = {k = 1}
        a {k = 2}
    ''', {'a': [{"k": 1}, {"k": 2}]}),
    ('''
        a = {k = 1}
        a = {k = 2}
    ''', {'a': {"k": 2}}),
])
def test_block(input, output):
    assert hcl2.loads(input) == output
