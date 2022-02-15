import random

print("***************************************")
print("* Bem vindo(a) ao jogo de adivinhação *")
print("***************************************")
print()

numero_secreto = 77
total_de_tentativas = 5
rodada = 1

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

print()
print("FIM DE JOGO!!!")