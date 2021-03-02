from re import search


def test_str_1(s='s'):
    assert len(s) < 255


def test_str_2():
    s = 'dfs'
    try:
        assert s[3]
    except IndexError:
        pass


def test_str_3():
    assert bool(search(r'rr', 'Array'))


def test_int_1(num=-100):
    assert num % 2 == 0


def test_int_2():
    try:
        assert 3 + '4'
    except TypeError:
        pass


def test_int_3():
    assert 0 + 100 == 100
