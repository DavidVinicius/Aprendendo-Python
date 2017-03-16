def soma_hipotenusas(x):
    ### ( 1 + n ) * n /2
    return ((1 + x) * x ) / 2

n = int(input("Digite um número inteiro:"))

print(soma_hipotenusas(n))