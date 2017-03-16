def imprime_matriz(matriz):

    for y in matriz:
        a = ""
        for x in y:
            a += str(x)
            a += " "
        print(a)



matriz = [[1,2,3],[4,5,6],[7,8,9]]
imprime_matriz(matriz)