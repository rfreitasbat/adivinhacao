import jogo

def jogar():
    print("***************************************")
    print("* Bem vindo(a) ao jogo de adivinhação *")
    print("***************************************")
    print()


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