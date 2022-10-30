import os 


def dicas(dica1, dica2, dica3):
    c=0





def tentativa(palavraChave):
    palavracodificada=("*"*len(palavraChave))
    contagemErros=0
    letraEscolhida=input("Digite a letra: ")
    if letraEscolhida in palavraChave:
        posicaoLetra_em_palavraChave=palavraChave.index(f'{letraEscolhida}')
        posicaoLetra_em_palavraCod=palavraChave[posicaoLetra_em_palavraChave]
        resultadoPalavra=palavracodificada.replace(f'{letraEscolhida}',f"{posicaoLetra_em_palavraCod}")
        print("Você acertou!")
        print(resultadoPalavra)
    
        



def opcoes():
    print("Pedir Dica = [x]")
    print("Tentar Letra = [z]")
    opcao_XouZ=input("Digite aqui: ")
    return opcao_XouZ
