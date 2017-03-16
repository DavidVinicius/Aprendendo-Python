n  = input("Digite o valor de n: ")
l = len(n)
n = int(n)

i = 0
a = 0

while i < l:
    a += (n % 100) % 10
    n = n // 10
    i = i + 1

print(a)