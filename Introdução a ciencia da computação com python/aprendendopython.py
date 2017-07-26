#Programa de equação de segundo grau

import math

a = float(input("Digite o termo a "))
b = float(input("Digite o termo b"))
c = float(input("Digite o termo c"))

delta = b**2 - (4*a*c)

print(delta)

if delta == 0:
    raiz1 = (-b) + math.sqrt(delta) / (2 * a)
    print("Delta tem apenas uma raiz", raiz1)
else:
    if delta < 0:
        print("Esta equação não possui raizes reais")
    else:
        raiz1 = -b + math.sqrt(delta)/ (2*a)
        raiz2 = -b - math.sqrt(delta)/ (2*a)
        print("A primeira raiz é ", raiz1)
        print("A segunda raiz é", raiz2)




