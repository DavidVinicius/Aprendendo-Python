while True:
    line = input("$ ")
    if line == "done":
        break
    if line == "soletrar()":
        nome = input("Digite o nome:")
        for i in nome:
            print(i)
    if line == "contar()":
        contar = input("Até quanto você quer que eu conte?")
        contar = int(contar)
        i = 0
        while i <= contar:
            print(i)
            i = i + 1


