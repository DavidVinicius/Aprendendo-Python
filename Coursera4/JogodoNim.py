def usuario_escolhe_jogada(n,m):
    x = int(input("Quantas peças vai retirar? "))

    while x > m or x > n or x == 0:
        print("")
        print("Oops! Jogada Inválida! Tente de novo.")
        x = int(input("Quantas peças vai retirar? "))
    if n - x == 0:
        print("")
        print("Você tirou ",x," peças")
        print("Fim de jogo! Você ganhou!")
    else:
        print("")
        print("Você tirou ", x, " peças")
        print("Agora restam ", (n - x ), "peças no tabuleiro")
    return x

def computador_escolhe_jogada(n,m):
    i = 0
    if n - m <= 0:
        i = n
    else:
        i = 0
        while i <= m:
            if (i + 1) > m:

                break
            elif n % (i + 1) == 0:
                if n % 2 != 0:
                    i = i + 1
                else:
                    i = i + 2
                break
            else:
                i = i + 1

    if n - i == 0:
        print("")
        print("O computador tirou ", i, " peças")
        print("Fim de Jogo !! O computador ganhou!!")

    else:
        print("")
        print("O computador tirou ", i, " peças")
        print("Agora resta ",(n - i)," peças no tabuleiro")

    if i == 0:
        i = m
    return i




def partida():
    n = int(input("Digite o número de peças inicial: "))
    m = int(input("Limite de peças por jogada? "))

    while m > n:
        print("")
        print("Limite de peças inválidos")
        m = int(input("Limite de peças por jogada? "))

    if n % (m + 1) == 0:
        print("")
        print("Você começa!")
        n = n -  usuario_escolhe_jogada(n,m)
        i = 1
    else:
        print("")
        print("O computador Começa!")
        n =  n - computador_escolhe_jogada(n,m)
        i = 2

    while n > 0:
        if i % 2 == 0:
            n = n - usuario_escolhe_jogada(n,m)
            if n == 0:
                print("")
                print("Fim de jogo! Você ganhou!")
                return False
        if i % 2 == 1:
            n = n - computador_escolhe_jogada(n,m)
            if n <= 0:
                print("")
                print("Fim do jogo! O computador ganhou!")
                return True
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