x = int(input("Digite a largura: "))
y = int(input("Digite o altura: "))

i = 1
j = 1

while j <= y:
    while i <= x:
        if i > 1 and i < x and j > 1 and j < y:
            print(" ",end="")
        else:
            print("#", end="")
        i = i + 1
    print("")
    i = 1
    j = j + 1
