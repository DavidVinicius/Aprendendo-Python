def maximo(x,y):
    if x >= y:
        return x
    else:
        return y


def test1():
    assert maximo(3,4) == 4


def test2():
    assert maximo(10,5) != 5