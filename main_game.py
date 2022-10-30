
from functions import dicas
from functions import tentativa
from functions import opcoes
import os 



def rodada():
    nameDesafiante=input("Digite o nome do desafiante: ")
    nameCompetidor=input("Digite o nome do competidor: ")
    os.system("cls")

    palavraChave=input("Digite a palavra:")
    dica1 = input("Digite aqui a primeira dica: ")
    dica2 = input("Digite aqui a segunda dica: ")
    dica3 = input("Digite aqui a terceira dica: ")
    os.system("cls")

    while True:
        contagemDica=0

        print("*"*len(palavraChave))
        opcoesDeJogo=opcoes ()

       #dica
        if opcoesDeJogo == "x": 
            if contagemDica < 3:
                dicas(dica1,dica2,dica3)
                print("Agora você deve obrigatóriamente tentar uma letra!")
                tentativa(palavraChave)
                contagemDica+=1
            else:
                print ("As dicas foram esgotadas!")
                return opcoes()

        #tentativa
        if opcoesDeJogo == "z":
            tentativa(palavraChave)
            break
rodada()

                    

            


