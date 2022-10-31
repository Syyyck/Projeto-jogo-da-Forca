
from functions import *
import os 

def inicioConfig():
    tentativasErradas=0

    print("Você deseja iniciar um novo jogo? Sim(1) ou Não(2)")
    perguntaIniciar=int(input(": "))
    if perguntaIniciar == 1:
        
        '''nameDesafiante=input("Digite o nome do desafiante: ")
        nameCompetidor=input("Digite o nome do competidor: ")
        os.system("cls")'''

        palavraChave=input("Digite a palavra:")
        '''
        dica1 = input("Digite aqui a primeira dica: ")
        dica2 = input("Digite aqui a segunda dica: ")
        dica3 = input("Digite aqui a terceira dica: ")
        os.system("cls")'''

        print("X"*len(palavraChave))
        print("Pedir Dica = [x]")
        print("Tentar Letra = [z]")
        try:
            opcao_XouZ=input("Digite aqui: ")# x para dica # z para tentar letra
        except:
            print("Digite um valor correto!")


        while True:
            if tentativasErradas < 5:

                #tentar letra
                if opcao_XouZ == "z":
                    tentativa(palavraChave)

                #dica
                '''if opcao_XouZ == "x": 
                    dicas(dica1, dica2, dica3)
                    if contagemDica < 3:
                        print("Agora você deve obrigatóriamente tentar uma letra!")
                        tentativa(palavraChave)
                        contagemDica+=1
                    else:
                        print ("As dicas foram esgotadas!")'''
                        
            else:
                break
inicioConfig()

            