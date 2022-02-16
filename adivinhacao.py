import jogo
import random

def jogar():
    print("***************************************")
    print("* Bem vindo(a) ao jogo de adivinhação *")
    print("***************************************")
    print()

    numero_secreto = random.randrange(1,101)
    total_de_tentativas = 0
    rodada = 1
    pontos = 100

    print("Escolha a dificuldade do jogo 1 - Fácil , 2 - Médio, 3 - Difícil", numero_secreto)
    dificuldade = int(input("Escolha a dificuldade: "))

    if(dificuldade == 1):
        total_de_tentativas = 20
    elif(dificuldade == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5

    for rodada in range(1, total_de_tentativas + 1):
        print("Tentativa {} de {}".format(rodada, total_de_tentativas))
        chute = input("Digite o seu número entre 1 e 100: ")
        numero_chute = int(chute)

        if(numero_chute < 1 or numero_chute > 100):
            print("Você digitou um numero invalido, digite um número entre 1 e 100")
            continue


        acertou_chute = numero_chute == numero_secreto
        chute_maior = numero_chute > numero_secreto
        chute_menor = numero_chute < numero_secreto

        if(acertou_chute):
            print("Você acertou!!!")
            print("voce chutou: ", chute, "e o numero erá: ", numero_secreto)
            break
        elif(chute_maior):
            print("Errou!!!!!!")
            print("Voce chutou: ", chute, "e o numero secreto é menor",)
        elif(chute_menor):
            print("Errou!!!!!!")
            print("Voce chutou: ", chute, "e o numero secreto é maior",)

        pontos_perdidos = abs(numero_secreto - numero_chute)
        pontos = pontos - pontos_perdidos
        if(pontos <= 0):
            pontos = 1

    print()
    print("FIM DE JOGO!!!")
    print("Pontuação restante {}!!!".format(pontos))
    print("O número secreto erá", numero_secreto)

    print()
    print("Deseja escolher o jogo?  (1) - SIM  (2) - Não")
    jogar_novamente = int(input("Digite seu escolha: "))
    if (jogar_novamente == 1):
        print()
        jogo.escolha_jogo()
        print()
    else:
        print("Valeu por Jogar")

if(__name__ == "__main__"):
    jogar()