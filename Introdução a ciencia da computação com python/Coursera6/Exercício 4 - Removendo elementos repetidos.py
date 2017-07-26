def remove_repetidos(x):
    aux = []
    copia = x[:]
    repetidos = []
    i = 0
    for y in x:
       if y == x[i]:
           aux.append(x[i])
           del x[i]
           if y in x:
               repetidos.append(y)
       else:
           repetidos.append(x[i])
       i = i + 1
    for y in copia:
        if y not in repetidos:
            repetidos.append(y)
    repetidos.sort()
    return repetidos


lista = [1,2,2,5,5,3,3,7,7,8,10,22,22,10]

print(remove_repetidos(lista))