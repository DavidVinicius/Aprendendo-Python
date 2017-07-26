def soma_elementos(x):
    a = 0
    for y in x:
        a = a + y
    return a

lista = [1,2,3,4,5]

print(soma_elementos(lista))