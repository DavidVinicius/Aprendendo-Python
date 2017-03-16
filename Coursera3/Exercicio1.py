n = int(input("Digite o valor de n: "))

if n == 0:
    n = 1
else:
    n = n

i = n

while i > 1:
    i = i - 1
    n = n * i

print(n)