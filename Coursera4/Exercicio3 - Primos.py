def maior_primo(n):
    n = int(n)
    while n < 2:
        n = int(input("Digite um numero maior ou igual a 2: "))

    def primo(n):
            i = n
            numDivisor = 0
            while i > 0:
             if n % i == 0:
                numDivisor = numDivisor + 1
             i = i - 1

            if numDivisor == 2:
                return True
            else:
                return False
    verifica = True

    while verifica:
        if primo(n) == True:
            verifica = False
        else:
            n = n - 1


    return n



