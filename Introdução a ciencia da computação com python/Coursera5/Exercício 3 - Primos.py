def éPrimo(x):
    fator = 2

    while x % fator != 0 and fator <= x/2:
        fator = fator + 1
    if x % fator == 0 and x != 2:
        return False
    else:
        return True
def n_primos(x):
    i = 1
    contadora = 0
    while i <= x:
        if éPrimo(i):
            contadora = contadora + 1
        i = i + 1
    return contadora

n = int(input("Digite um número inteiro maior ou igual a 2: "))

print(n_primos(n))