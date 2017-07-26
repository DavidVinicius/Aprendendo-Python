a = int(input("Digite o primeiro termo"))
b = int(input("Digite o segundo termo"))
c = int(input("Digite o terceiro termo"))

discriminante = (b**2) - 4*a*c
raiz1         = (-b + discriminante)/(2*a)
raiz2         = (b + discriminante)/(2*a)

print(discriminante)
print(raiz1)
print(raiz2)

if discriminante < 0:
    print("Essa equação não possui raizes reais")
else:
    if discriminante == 0:
        print("Essa equação te somente uma raiz: ", raiz1)
    else:
        if raiz1 > raiz2:
            print("As raizes dessa equação é ", raiz1, " ,",raiz2 )
        else:
            print("As raizes dessa equação é ", raiz2, " ,", raiz1)
