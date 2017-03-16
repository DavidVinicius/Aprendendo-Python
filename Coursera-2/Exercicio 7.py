import math

xa = int(input("Digite o primeiro ponto de x"))
ya = int(input("Digite o primeiro ponto de y"))

print("O primeiro ponto é : (",xa,",",ya,")")

xb = int(input("Digite o segundo ponto de x"))
yb = int(input("Digite o segundo ponto de y"))

print("O segundo ponto é: (",xb,",",yb,")")

catetoA = xa - xb
catetoB = ya - yb

hipotenusa = catetoA**2 + catetoB**2

hipotenusa = math.sqrt(hipotenusa)

if hipotenusa >= 10 :
    print("Longe")
else:
    print("perto")