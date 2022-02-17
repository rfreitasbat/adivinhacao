import jogo

def jogar():
    print("***************************************")
    print("* Bem vindo(a) ao jogo de adivinhação *")
    print("***************************************")
    print()

    palavra_secreta = "banana"
    letras_acertadas = ["_","_","_","_","_","_"]

    enforcou = False
    acertou = False
    print(letras_acertadas)

    while(not enforcou and not acertou):

        chute = input("Digite uma letra: ").strip()

        index = 0
        for letra in palavra_secreta:
            if(chute.upper() == letra.upper()):
                print("Encontrei a letra {} na posição {}".format(letra, index))
                letras_acertadas[index] = chute
            index = index + 1

        print(letras_acertadas)

    print("FIM DE JOGO!!!")

    print()
    print("Deseja escolher o jogo?  (1) - SIM  (2) - Não")
    jogar_novamente = int(input("Digite seu escolha: "))
    if(jogar_novamente == 1):
        print()
        jogo.escolha_jogo()
        print()
    else:
        print("Valeu por Jogar")

if(__name__ == "__main__"):
    jogar()