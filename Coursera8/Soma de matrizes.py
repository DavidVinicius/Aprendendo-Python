def soma_matrizes(m1,m2):
    if len(m1) != len(m2) or len(m1[0]) != len(m2[0]):
        return False
    else:
        i = 0
        for y in m1:
            j = 0
            for x in y:
                m2[i][j] += int(x)
                j = j + 1
            i = i + 1
        return m2

matrizA = [[1,2,3],[4,5,6]]
matrizB = [[2,3,4],[5,6,7]]

print(soma_matrizes(matrizA,matrizB))