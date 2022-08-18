from dcache.keys import dhash


def func(*args, **kwargs):
    pass


def func1(*args, **kwargs):
    pass


def func2(*args, **kwargs):
    pass


def test_same_functions():
    assert dhash(func) == dhash(func)
    assert dhash(func1) == dhash(func1)
    assert dhash(func2) == dhash(func2)


def test_different_funcions():
    assert dhash(func1) != dhash(func2)


def test_same_args():
    assert dhash(func, "arg1") == dhash(func, "arg1")
    assert dhash(func, "arg2") == dhash(func, "arg2")


def test_different_args():
    assert dhash(func, "arg1") != dhash(func, "arg2")
    assert dhash(func, "arg2") != dhash(func, "arg1")


def test_same_kwargs():
    assert dhash(func, same="same") == dhash(func, same="same")


def test_different_kwargs():
    assert dhash(func, kone="same") != dhash(func, ktwo="same")
    assert dhash(func, same="diff1") != dhash(func, same="diff2")
    assert dhash(func, kone="diff1") != dhash(func, ktwo="diff2")
