import json
import pytest

from runflow import hcl2

def test_module():
    assert isinstance(hcl2.loads('a=1'), hcl2.Module)

@pytest.mark.parametrize('input, output', [
    ('1', 1),
    ('true', True),
    ('false', False),
    ('1.0', 1.0),
    ('0.0', 0.0),
    ('null', None),
    ('[]', []),
    ('[1,2,3]', [1,2,3]),
    ('{}', {}),
    ('{"k" = 1}', {'k': 1}),
    ('{"k" : 1}', {'k': 1}),
    ('{k = 1}', {'k': 1}),
    ('"${x}"', '"${x}"'),
    ('"${x}"', '"${x}"'),
])
def test_expression(input, output):
    assert hcl2.loads(input, start='eval') == output

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
    assert hcl2.loads('sum = 1 + addend') == {'sum': hcl2.Interpolation(
        hcl2.Operation([1, '+', hcl2.Identifier('addend')])
    )}
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

def test_attr_splat():
    assert hcl2.loads('a = b.*.c.d') == {'a': hcl2.Interpolation(
        hcl2.Splat('b', ['c', 'd'])
    )}
    assert hcl2.loads('a = b.*.c.d[0]') == {'a': hcl2.Interpolation(
        hcl2.GetIndex(hcl2.Splat('b', ['c', 'd']), 0)
    )}

def test_full_splat():
    assert hcl2.loads('a = b[*].c.d') == {'a': hcl2.Interpolation(
        hcl2.Splat('b', ['c', 'd'])
    )}
    assert hcl2.loads('a = b[*].c.d[0]') == {'a': hcl2.Interpolation(
        hcl2.Splat('b', ['c', 'd', 0])
    )}

def test_func_call():
    assert hcl2.loads('a = randint()') == {'a': hcl2.Interpolation(
        hcl2.Call('randint', [])
    )}
    assert hcl2.loads('shouty_message = upper(message)') == {
        'shouty_message': hcl2.Interpolation(
            hcl2.Call('upper', [hcl2.Identifier('message')])
        )
    }

def test_conditional():
    assert hcl2.loads('a = b ? 1 : 0') == {'a': hcl2.Interpolation(
        hcl2.Conditional(
            hcl2.Identifier('b'),
            1,
            0
        )
    )}

def test_bin_or():
    assert hcl2.loads('a = true || false') == {'a': hcl2.Interpolation(
        hcl2.Operation([True, '||', False])
    )}

def test_bin_and():
    assert hcl2.loads('a = true && false') == {'a': hcl2.Interpolation(
        hcl2.Operation([True, '&&', False])
    )}

def test_bin_and_or():
    assert hcl2.loads('a = true || true && false') == {'a': hcl2.Interpolation(
        hcl2.Operation([True, '||', hcl2.Operation([True, '&&', False])])
    )}
    assert hcl2.loads('a = true && true || false') == {'a': hcl2.Interpolation(
        hcl2.Operation([hcl2.Operation([True, '&&', True]), '||', False])
    )}

def test_bin_eq():
    assert hcl2.loads('a = true == false') == {'a': hcl2.Interpolation(
        hcl2.Operation([True, '==', False])
    )}
    assert hcl2.loads('a = true == false != false') == {'a': hcl2.Interpolation(
        hcl2.Operation([True, '==', False, '!=', False])
    )}

def test_arithmetic():
    assert hcl2.loads('a=1*(2+3)') == {'a': hcl2.Interpolation(
        hcl2.Operation([1, '*', hcl2.Operation([2, '+', 3])])
    )}
    assert hcl2.loads('a=1*2+3') == {'a': hcl2.Interpolation(
        hcl2.Operation([hcl2.Operation([1, '*', 2]), '+', 3])
    )}
    assert hcl2.loads('a=1+2*3') == {'a': hcl2.Interpolation(
        hcl2.Operation([1, '+', hcl2.Operation([2, '*', 3])])
    )}

def test_unary():
    assert hcl2.loads('a= (-1)+(-2)') == {'a': hcl2.Interpolation(
        hcl2.Operation([hcl2.Operation([0, '-', 1]), '+', hcl2.Operation([0, '-', 2])])
    )}
    assert hcl2.loads('a= !false') == {'a': hcl2.Interpolation(
        hcl2.Not(False)
    )}

def test_list_expr():
    assert hcl2.loads('a = [for x in xs: x]') == {'a': hcl2.Interpolation(
        hcl2.ListExpr(hcl2.Identifier('x'), hcl2.Identifier('xs'), hcl2.Identifier('x'), None)
    )}
    assert hcl2.loads('a = [for x in xs: x if x]') == {'a': hcl2.Interpolation(
        hcl2.ListExpr(
            hcl2.Identifier('x'),
            hcl2.Identifier('xs'),
            hcl2.Identifier('x'),
            hcl2.Identifier('x'),
        )
    )}

def test_dict_expr():
    assert hcl2.loads('a = {for x in xs: x => true}') == {'a': hcl2.Interpolation(
        hcl2.DictExpr(
            hcl2.Identifier('x'),
            hcl2.Identifier('xs'),
            hcl2.Identifier('x'),
            True,
            None)
    )}
    assert hcl2.loads('a = {for x in xs: x => true if x}') == {'a': hcl2.Interpolation(
        hcl2.DictExpr(
            hcl2.Identifier('x'),
            hcl2.Identifier('xs'),
            hcl2.Identifier('x'),
            True,
            hcl2.Identifier('x'))
    )}

def test_heredoc_template():
    assert hcl2.loads("""
a = <<EOT
HELLO
WORLD
EOT""") == {'a': "HELLO\nWORLD"}
    assert hcl2.loads("""
a = <<-EOT
    HELLO
      WORLD
EOT""") == {'a': "HELLO\n  WORLD"}
