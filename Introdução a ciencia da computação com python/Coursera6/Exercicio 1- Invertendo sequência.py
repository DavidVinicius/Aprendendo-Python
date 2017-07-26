n = int(input("Digite um numero ou 0 para sair:"))
lista = []

while n != 0:
    if n != 0:
        lista.append(n)
    else:
        break
    n = int(input("Digite um numero ou 0 para sair:"))


lista.reverse()

for x in lista:
    print(x)
