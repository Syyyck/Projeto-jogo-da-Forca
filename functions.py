import os
from time import sleep 


def inicioConfig():
    try:
        nomeDesafiante=input("Digite o nome do desafiante: ")
        nomeCompetidor=input("Digite o nome do competidor: ")
        apagarSerial()

        palavraChave=input("Digite a palavra:")
        palavraChave=palavraChave.upper()
        PalavraRegistradas(palavraChave)
        dica1 = input("Digite aqui a primeira dica: ")
        dica2 = input("Digite aqui a segunda dica: ")
        dica3 = input("Digite aqui a terceira dica: ")
        apagarSerial()
    except:
        print("Digite valores corretos!")
        apagarSerial()
        return inicioConfig()
    return palavraChave, dica1, dica2, dica3, nomeCompetidor, nomeDesafiante

   
    
def dicas(dica1, dica2, dica3,contagemDica):

    if contagemDica == 1:
        print(f'Dica 1: {dica1}')
    elif contagemDica == 2:
        print(f'Dica 2: {dica2}')
    elif contagemDica == 3:
        print(f'Dica 3: {dica3}')

def tentativa(palavraChave,tentativasErradas,palavracodificada):
    letraEscolhida=input("Digite a letra: ")
    if len(letraEscolhida) > 1:
        print("Digite apenas uma letra")
        apagarSerial()
        return tentativa(palavraChave,tentativasErradas,palavracodificada)
    letraEscolhida=letraEscolhida.upper()
    palavracodificada = list(palavracodificada)

    #analisando letra
    if letraEscolhida in palavracodificada:
        print("Você já digitou esta letra antes!")
        sleep(0.50)
        return palavracodificada,tentativasErradas

    elif letraEscolhida in palavraChave:
        print("Você descobriu uma letra!")
        for i in range(len(palavraChave)):
            if palavraChave[i] == letraEscolhida:
                palavracodificada[i] = letraEscolhida
        return palavracodificada,tentativasErradas

     #errou
    else:
        print("Esta letra não pertence a palavra!")
        tentativasErradas+=1
        print("Você ainda possui: ",5-(tentativasErradas)," chances")
        return palavracodificada,tentativasErradas


def opcoes():
    
    print("Pedir Dica = [x]")
    print("Tentar Letra = [z]")
    opcao_XouZ=input("Digite aqui: ")
    return opcao_XouZ


def apagarSerial():
    os.system("cls")


def historicoPartidas(palavraChave,desafiante, competidor,ganhador):
    try:
        escreverHist = open("dados_anteriores", "a+")
        escreverHist.write(f'''Desafiante: {desafiante} -- Competidor: {competidor} 
        -- Palavra:{palavraChave} -- Ganhador:{ganhador}\n''')
        escreverHist.close()

        leituraLinha=open("dados_anteriores","r")
        partidas=leituraLinha.read()
        leituraLinha.close()

        print('Histótrico de partidas anteriores:')
        print(partidas)
        sleep(5)
    except:
        print("Não foi possivel acessar o histórico de partidas")

def PalavraRegistradas(palavraChave):
    #Futuramente incrementar opção computadorXjogador
    escreverLista=open("palavras_anteriores","a+")
    escreverLista.write(palavraChave)
    escreverLista.close()
    
    
