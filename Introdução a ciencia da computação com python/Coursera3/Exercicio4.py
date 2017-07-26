n = input("Digite o numero n: ")
l = len(n)
n = int(n)

i = 0
verifica = 0

while i < l:
    a = n % 10
    b = (n // 10) % 10
    if a == b:
        verifica = verifica + 1

    i = i + 1
    n = n // 10

if verifica > 0:
    print("sim")
else:
    print("Não")