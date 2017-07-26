def fizzbuzz(x):
    if x % 3 == 0 and x % 5 ==0:
        return "FizzBuzz"
    else:
        if x % 3 == 0:
            return "Fizz"
        else:
            if x % 5 == 0:
               return "Buzz"
            else:
                return x


def test_exe1():
    assert fizzbuzz(30) == "FizzBuzz"

def test_exe2():
    assert fizzbuzz(4) == 4

def test_exe3():
    assert fizzbuzz(5) == "Buzz"