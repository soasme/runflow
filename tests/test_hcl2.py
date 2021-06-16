from datetime import datetime
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
])
def test_expression(input, output):
    assert hcl2.loads(input, start='eval') == output
    assert isinstance(hcl2.loads(input, start='eval'), type(output))

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

def test_heredoc():
    assert hcl2.loads('''a = <<EOT
XXX
YYY
EOT''') == {'a': 'XXX\nYYY'}
    assert hcl2.loads('''a = <<EOT
  XXX
  YYY
EOT''') == {'a': '  XXX\n  YYY'}
    assert hcl2.loads('''a = <<-EOT
  XXX
  YYY
EOT''') == {'a': 'XXX\nYYY'}
    assert hcl2.loads('''a = <<-EOT
  XXX
    YYY
EOT''') == {'a': 'XXX\n  YYY'}


def test_eval():
    assert hcl2.eval(hcl2.loads('a = b'), {'b': 1}) == {'a': 1}
    assert hcl2.eval(hcl2.loads('a = var.b'), {'var': {'b': 1}}) == {'a': 1}
    assert hcl2.eval(hcl2.loads('a = b.0'), {'b': [1]}) == {'a': 1}
    with pytest.raises(IndexError):
        assert hcl2.eval(hcl2.loads('a = b.1'), {'b': [1]}) == {'a': 1}
    with pytest.raises(TypeError):
        assert hcl2.eval(hcl2.loads('a = b.c'), {'b': [1]}) == {'a': 1}
    assert hcl2.eval(hcl2.loads('a {k=b}\na {k=b}'), {'b': 1}) == {'a': [
        {'k': 1}, {'k': 1}
    ]}
    assert hcl2.eval(hcl2.loads('a {k=b}\na {k=b+1}'), {'b': 1}) == {'a': [
        {'k': 1}, {'k': 2}
    ]}
    assert hcl2.eval(hcl2.loads('a = !b'), {'b': True}) == {'a': False}
    assert hcl2.eval(hcl2.loads('a = (!b) || (!c)'), {'b': True, 'c': False}) == {'a': True}
    # TBD: need fix it
    # assert hcl2.eval(hcl2.loads('a = !b || !c'), {'b': True, 'c': False}) == {'a': True}
    assert hcl2.eval(hcl2.loads('a = b && c'), {'b': True, 'c': True}) == {'a': True}
    assert hcl2.eval(hcl2.loads('a = b && c'), {'b': True, 'c': False}) == {'a': False}
    assert hcl2.eval(hcl2.loads('a = b && c'), {'b': False, 'c': False}) == {'a': False}
    assert hcl2.eval(hcl2.loads('a = b && c'), {'b': False, 'c': True}) == {'a': False}
    assert hcl2.eval(hcl2.loads('a = b || c'), {'b': True, 'c': True}) == {'a': True}
    assert hcl2.eval(hcl2.loads('a = b || c'), {'b': True, 'c': False}) == {'a': True}
    assert hcl2.eval(hcl2.loads('a = b || c'), {'b': False, 'c': False}) == {'a': False}
    assert hcl2.eval(hcl2.loads('a = b || c'), {'b': False, 'c': True}) == {'a': True}
    assert hcl2.eval(hcl2.loads('a = b == c == d'), {'b': 1, 'c': 1, 'd': 1}) == {'a': True}
    assert hcl2.eval(hcl2.loads('a = b == c == d'), {'b': 1, 'c': 1, 'd': 2}) == {'a': False}
    assert hcl2.eval(hcl2.loads('a = b == c == d'), {'b': 2, 'c': 1, 'd': 1}) == {'a': False}
    with pytest.raises(ZeroDivisionError):
        assert hcl2.eval(hcl2.loads('a = b / 0'), {'b': 1})
    assert hcl2.eval(hcl2.loads('a = b / 2'), {'b': 4}) == {'a': 2}
    assert hcl2.eval(hcl2.loads('a = b / 2.0'), {'b': 4}) == {'a': 2.0}
    assert hcl2.eval(hcl2.loads('a = b % 3'), {'b': 5}) == {'a': 2}
    assert hcl2.eval(hcl2.loads('a = b * 3'), {'b': 5}) == {'a': 15}
    assert hcl2.eval(hcl2.loads('a = b+(c*d)'), {'b': 1, 'c': 2, 'd': 3}) == {'a': 7}
    assert hcl2.eval(hcl2.loads('a = b+c*d'), {'b': 1, 'c': 2, 'd': 3}) == {'a': 7}
    assert hcl2.eval(hcl2.loads('a = (b+c)*d'), {'b': 1, 'c': 2, 'd': 3}) == {'a': 9}
    assert hcl2.eval(hcl2.loads('a = b*(c+d)'), {'b': 2, 'c': 1, 'd': 3}) == {'a': 8}
    assert hcl2.eval(hcl2.loads('a = b*c+d'), {'b': 2, 'c': 1, 'd': 3}) == {'a': 5}
    assert hcl2.eval(hcl2.loads('a = b.*.c'), {
        'b': [{'c': 1}, {'c': 2}]
    }) == {'a': [1, 2]}
    assert hcl2.eval(hcl2.loads('a = b[*].c[0]'), {
        'b': [{'c': [1]}, {'c': [2]}]
    }) == {'a': [1, 2]}
    assert hcl2.eval(hcl2.loads('a = b[*].c.0'), {
        'b': [{'c': [1]}, {'c': [2]}]
    }) == {'a': [1, 2]}
    assert hcl2.eval(hcl2.loads('a = b.*.c[0]'), {
        'b': [{'c': [1]}, {'c': [2]}]
    }) == {'a': [1]}
    assert hcl2.eval(hcl2.loads('a = b.*.c[0]'), {
        'b': [{'c': 1}, {'c': 2}]
    }) == {'a': 1}

    assert hcl2.eval(hcl2.loads('a = [for x in xs: x.key]'), {
        'xs': [{'key': 1}, {'key': 2}]
    }) == {'a': [1, 2]}
    assert hcl2.eval(hcl2.loads('a = [for i, x in xs: x.key * (i+1)]'), {
        'xs': [{'key': 1}, {'key': 2}]
    }) == {'a': [1, 4]}
    assert hcl2.eval(hcl2.loads('a = [for x in xs: x.key if x.key >= 2]'), {
        'xs': [{'key': 1}, {'key': 2}, {'key': 3}]
    }) == {'a': [2, 3]}
    assert hcl2.eval(hcl2.loads('a = {for x in xs: x.key => x.key * 2}'), {
        'xs': [{'key': 1}, {'key': 2}]
    }) == {'a': {1: 2, 2: 4}}
    assert hcl2.eval(hcl2.loads('a = {for i, x in xs: x.key => x.key * (i+2)}'), {
        'xs': [{'key': 1}, {'key': 2}]
    }) == {'a': {1: 2, 2: 6}}

    assert hcl2.eval(hcl2.loads('a = [for x in xs: x]'), {
        'xs': {'k1': 1, 'k2': 2},
    }) == {'a': ['k1', 'k2']}
    assert hcl2.eval(hcl2.loads('a = [for k, v in xs: k if v > 1]'), {
        'xs': {'k1': 1, 'k2': 2},
    }) == {'a': ['k2']}
    assert hcl2.eval(hcl2.loads('a = {for k in xs: k => k}'), {
        'xs': {'k1': 1, 'k2': 2},
    }) == {'a': {'k1': 'k1', 'k2': 'k2'}}
    assert hcl2.eval(hcl2.loads('a = {for k, v in xs: v => k}'), {
        'xs': {'k1': 1, 'k2': 2},
    }) == {'a': {1: 'k1', 2: 'k2'}}

    assert set(hcl2.eval(hcl2.loads('a = [for x in xs: x]'), {
        'xs': {'k1', 'k2'},
    })['a']) == {'k1', 'k2'}
    assert set(hcl2.eval(hcl2.loads('a = [for k, v in xs: k if v]'), {
        'xs': {'k1', 'k2', False},
    })['a']) == {'k1', 'k2'}
    assert hcl2.eval(hcl2.loads('a = {for k in xs: k => k}'), {
        'xs': {'k1', 'k2'},
    }) == {'a': {'k1': 'k1', 'k2': 'k2'}}
    assert hcl2.eval(hcl2.loads('a = {for k, v in xs: v => k}'), {
        'xs': {'k1', 'k2'},
    }) == {'a': {'k1': 'k1', 'k2': 'k2'}}

    assert hcl2.eval(hcl2.loads('a = b?c:d'), {'b': True, 'c': 1, 'd': 2}) == {'a': 1}
    assert hcl2.eval(hcl2.loads('a = b?c:d'), {'b': False, 'c': 1, 'd': 2}) == {'a': 2}

    assert hcl2.eval(hcl2.loads('a = lower(b)'), {'b': 'X'}) == {'a': 'x'}
    assert hcl2.eval(hcl2.loads('a = upper(b)'), {'b': 'x'}) == {'a': 'X'}
    assert hcl2.eval(hcl2.loads('a = float(b)'), {'b': 1}) == {'a': 1.0}
    assert hcl2.eval(hcl2.loads('a = int(b)'), {'b': 1.0}) == {'a': 1}
    assert hcl2.eval(hcl2.loads('a = str(b)'), {'b': 1.0}) == {'a': '1.0'}
    assert hcl2.eval(hcl2.loads('a = $math:ceil(b)'), {'b': 1.9}) == {'a': 2.0}
    assert hcl2.eval(hcl2.loads('a = list($itertools:chain.from_iterable(b))'), {
        'b': ['ABC', 'DEF']
        }) == {'a': ['A', 'B', 'C', 'D', 'E', 'F']}
    assert hcl2.eval(hcl2.loads('a = $datetime:datetime(year, month, day)'), {
        'year': 1989, 'month': 6, 'day': 4,
    }) == {'a': datetime(1989, 6, 4) }
    # assert hcl2.eval(hcl2.loads('a = "${$math:ceil(b)}"'), {'b': 1.9}) == {'a': 2.0}
