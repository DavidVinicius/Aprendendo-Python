numero = input("Digite um numero inteiro")
comprimento = len(numero)
numero = int(numero)

if comprimento > 1:
    numero = ((numero % 1000) % 100 ) // 10
    print (" A dezena é ", numero)
else:
    print("O digito das dezenas é 0")
