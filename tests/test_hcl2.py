import json
import pytest

from runflow import hcl2

def test_module():
    assert isinstance(hcl2.loads('a=1'), hcl2.Module)

@pytest.mark.parametrize('input, output', [
    ('a = 1', {'a': 1}),
    ('a = true', {'a': True}),
    ('a = false', {'a': False}),
    ('a = 1.0', {'a': 1.0}),
    ('a = null', {'a': None}),
    # ('a = 1e7', {'a': 1e7}), This seems wrong. python-hcl2 needs fix it.
    ('a = []', {'a': []}),
    ('a = [1,2,3]', {'a': [1,2,3]}),
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

def test_interpolation():
    assert hcl2.loads('message = "Hello, ${name}!"') == {
            'message': "Hello, ${name}!"}
    assert hcl2.loads('shouty_message = upper(message)') == {
            'shouty_message': hcl2.Interpolation('upper(message)')}
    assert hcl2.loads('sum = 1 + addend') == {'sum': hcl2.Interpolation('1 + addend')}
    assert hcl2.loads('a = var.b') == {
        'a': hcl2.Interpolation(
            hcl2.GetAttr(hcl2.Identifier('var'), hcl2.Identifier('b'))
        )
    }

def test_getindex():
    assert hcl2.loads('a = b[1]') == {'a': hcl2.Interpolation(hcl2.GetIndex('b', 1))}
    assert hcl2.loads('a = b[1][2]') == {'a': hcl2.Interpolation(hcl2.GetIndex(hcl2.GetIndex('b', 1), 2))}
    assert hcl2.loads('a = b.10') == {'a': hcl2.Interpolation(hcl2.GetIndex('b', 10))}
    assert hcl2.loads('a = b.1.2') == {'a': hcl2.Interpolation(hcl2.GetIndex(hcl2.GetIndex('b', 1), 2))}
    assert hcl2.loads('a = b["key"]') == {'a': hcl2.Interpolation(hcl2.GetIndex('b', 'key'))}

def test_getattr():
    assert hcl2.loads('a = b.key') == {'a': hcl2.Interpolation(hcl2.GetAttr('b', 'key'))}
