from runflow.hcl2 import loads

def test_int_lit():
    assert loads('a = 123') == {'a': 123}

def test_float_lit():
    assert loads('a = 1.23') == {'a': 1.23}

def test_true_false_null():
    assert loads('a = true') == {'a': True}
    assert loads('a = false') == {'a': False}
    assert loads('a = null') == {'a': None}
    assert loads('a = (true)') == {'a': True}
    assert loads('a = (false)') == {'a': False}
    assert loads('a = (null)') == {'a': None}

def test_object():
    assert loads('a = {}') == {'a': {}}
    assert loads('a = { b = 1 }') == {'a': {'b': 1}}
    assert loads('''
    a = {
        b = 1
        c = { key = "value" }
    }''') == {'a': {'b': 1, 'c': {'key': 'value'}}}

def test_block():
    assert loads('''
    a { name = "1st" }
    a { name = "2nd" }
    ''') == {'a': [{'name': '1st'}, {'name': '2nd'}]}

def test_functional_call():
    data = loads('a = tojson({})')
    assert data['a'].name == 'tojson'
    assert data['a'].args == [{}]

    data = loads('a = tojson(var.data)')
    assert data['a'].name == 'tojson'
    assert data['a'].args == ['var.data']
