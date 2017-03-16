def maior_elemento(x):
    a = 0
    for y in x:
        if y > a:
            a = y
           
    return a


lista = [1,2,3,4]

print(maior_elemento(lista))