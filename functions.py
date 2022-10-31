import os
from time import sleep 



def dicas(dica1, dica2, dica3):
    contagemDica=0
    return contagemDica

def tentativa(palavraChave):
    palavracodificada=list("X"*len(palavraChave))
    letraEscolhida=input("Digite a letra: ")
    tentativasErradas=0
    letraCorreta=[]

    #acertou
    for i in range(len(palavraChave)):
        if palavraChave[i] == letraEscolhida:
            palavracodificada[i] = letraEscolhida
            letraCorreta.append(letraEscolhida)

    palavraResultado = " ".join(palavracodificada) #Convert lista em str
    if letraEscolhida in palavraChave:
        print("Você descobriu uma letra!")
    
    #errou
    else:
        print("Esta letra não pertence a palavra!")
        tentativasErradas+=1
        print("Você ainda possui: ",5-(tentativasErradas)," chances")
    
    return opcoes(palavraResultado),tentativasErradas


def errosTentativas(letrasErradas):
    numeroErros=letrasErradas
    return numeroErros
    
    
def opcoes(palavraResultado):
    print(palavraResultado)
    print("Pedir Dica = [x]")
    print("Tentar Letra = [z]")
    opcao_XouZ=input("Digite aqui: ")
    return opcao_XouZ
