def maximo(x,y,z):
    if x > y and x > z:
        return x
    else:
        if y > z and y > x:
            return y
        else:
            return z

def test1():
    assert maximo(30,25,15) == 30

def test2():
    assert maximo(0,1,-1) == 1