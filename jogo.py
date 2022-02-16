import adivinhacao
import forca

def escolha_jogo():
    print("***************************************")
    print("*********** Escolha o Jogo ************")
    print("***************************************")
    print()

    print("Escolha entre 1 e 2")

    escolha = int(input("(1) - Adivinhação   (2) - Forca"))

    if(escolha == 1):
        print("adivinhação")
        adivinhacao.jogar()
    elif(escolha == 2):
        print("Forca")
        forca.jogar()

if(__name__ == "__main__"):
    escolha_jogo()
