n = int(input("Digite um número inteiro: "))

i = n
numDivisores = 0

while i > 0:
    if n % i == 0:
        numDivisores = numDivisores + 1
    i = i - 1

if numDivisores == 2 or n == 1:
    print("Primo")
else:
    print("Não primo")