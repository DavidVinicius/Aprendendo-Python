def vogais(x):
    if x.lower() == "a" or x.lower() == "e" or x.lower() == "i" or x.lower() == "o" or x.lower() == "u":
        return True
    else:
        return False

def test1():
    assert vogais("A") == True


def test2():
    assert vogais("c") == False