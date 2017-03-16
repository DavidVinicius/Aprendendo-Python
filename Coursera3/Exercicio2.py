n = int(input("Digite o valor de n: "))

i = 1
contadora = 0

while contadora < n:
    if i % 2 == 1:
        print(i)
        contadora = contadora + 1
    i = i + 1
