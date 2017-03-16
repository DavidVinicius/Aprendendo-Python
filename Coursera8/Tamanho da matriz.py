def dimensoes(matriz):
    i = 0
    j = 0
    for x in matriz:
        for y in x:
            j = j + 1
        i = i + 1
    j = j // i

    print(i,"X",j,sep="")


