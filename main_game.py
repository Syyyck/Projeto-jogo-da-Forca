
from functions import *
import os 


def funcaoConst():
    def inicio():
        rodada=True
        contagemDica=1
        chancesPerdidas=0

        palavraChave, dica1, dica2, dica3, nomeCompetidor, nomeDesafiante = inicioConfig()
        palavraChave=palavraChave.upper()
        palavraoculta =("#"*(len(palavraChave)))
                
        while (rodada):

             #Verificar Tentativas
            if chancesPerdidas < 5:
                opcao=opcoes()

                #tentar letra
                if opcao == "z":
                    apagarSerial()
                    palavraoculta, chancesPerdidas = tentativa(palavraChave,chancesPerdidas,palavraoculta)
                    palavraoculta="".join(palavraoculta)
                    print (palavraoculta)

                    if palavraoculta == palavraChave:
                        vencedor=nomeCompetidor
                        print("O Compedidor ganhou!")
                        historicoPartidas(palavraChave, nomeDesafiante, nomeCompetidor, vencedor)
                        rodada = False

                #dica
                elif opcao == "x":
                    apagarSerial()
                    if contagemDica < 3:
                        dicas(dica1, dica2, dica3,contagemDica)
                        print("Agora você deve obrigatóriamente tentar uma letra!")
                        palavraoculta, chancesPerdidas = tentativa(palavraChave,chancesPerdidas,palavraoculta)
                        palavraoculta="".join(palavraoculta)
                        contagemDica+=1
                        print (palavraoculta)
                    else:
                        print ("As dicas foram esgotadas!")
                else:
                    print("Digite um valor válido")
                    print("______________")

            else: 
                apagarSerial()
                print("O competidor perdeu!")
                sleep(0.70)
                apagarSerial()
                vencedor=nomeDesafiante
                historicoPartidas(palavraChave, nomeDesafiante, nomeCompetidor, vencedor)
                rodada = False

    apagarSerial()

    try:
        print("Deseja iniciar o jogo? Sim(1) Não(2)")
        exit=int(input(": " ))
    except: 
        print("Digite um valor correto!")
        sleep(0.30)
        
    if exit == 1:
        inicio()
    elif exit == 2:
        print("Volte Sempre!")
        sleep(0.70)
        apagarSerial()


while True:
    sleep(1)
    funcaoConst()
            
        
            