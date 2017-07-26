def computador_escolhe_jogada(n,m):
    i = 1
    while i < m:
        if (n - i) % (m + 1) == 0:
            return i
        else:
            i = i + 1
    return i


def usuario_escolhe_jogada(n,m):
    print("")
    print("Você pode retirar",m," peças")
    jogada = int(input("Quantas peças vai retirar? "))
    while jogada > m or jogada <= 0:
        print("Jogada inválida")
        print("Você pode retirar", m, " peças")
        jogada = int(input("Quantas peças vai retirar? "))
        print("")

    return jogada

def partida():
    print("******")
    n = int(input("Digite o número de peças inicial: "))
    m = int(input("Limite de peças por jogada? "))
    print("******")

    while m > n:
        print("")
        print("Limite de peças inválidos")
        m = int(input("Limite de peças por jogada? "))

    if n % (m + 1) == 0:
        print("")
        print("Você começa!")
        jogadaUsuario = usuario_escolhe_jogada(n,m)
        print("Você retirou ",jogadaUsuario,"peças")
        n = n -  jogadaUsuario
        print("Restam ",n," peças")
        print("")
        i = 1
    else:
        print("")
        print("O computador Começa!")
        jogadaComputador = computador_escolhe_jogada(n,m)
        print("O computador retirou ",jogadaComputador,"pecas")
        n =  n - jogadaComputador
        print("Restam ",n,"pecas")
        print("")
        i = 2

    while n > 0:
        if i % 2 == 0:

            jogadaUsuario = usuario_escolhe_jogada(n, m)

            print("Você retirou ", jogadaUsuario, "peças")

            n = n - jogadaUsuario

            if n == 0:
                print("")
                print("Fim de jogo! Você ganhou!")
                return False

            print("Restam ", n, " peças")
            print("")

        if i % 2 == 1:

            jogadaComputador = computador_escolhe_jogada(n, m)

            print("O computador retirou ", jogadaComputador, "pecas")

            n = n - jogadaComputador

            if n == 0:
                print("")
                print("Fim do jogo! O computador ganhou!")
                return True

            print("Restam ", n, "pecas")
            print("")

        i = i  + 1

def campeonato():
    print(" Bem-vindo ao jogo do NIM! escolha:")
    print(" 1 - para jogar uma partida isolada")
    print(" 2 - para jogar um campeonato")
    print("\n")

    p = int(input(""))



    if p == 1:
        partida()
    else:
        i = 1
        C = 0
        U = 0

        while i <= 3:
            print("")
            print("")
            print("****** Rodada ",i," *******")
            if partida():
                C = C + 1
            else:
                U = U + 1
            i = i + 1
        print("")
        print("")
        print("***** FINAL DO CAMPEONATO *****")
        print("Placar: Você ",U," X ", C," Computador")

campeonato()