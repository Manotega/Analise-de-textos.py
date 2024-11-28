import re

def le_assinatura():
    #'''A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada com os textos fornecidos'''
    print("Bem-vindo ao detector automático de COH-PIAH.")
    print("Informe a assinatura típica de um aluno infectado:")

    wal = float(input("Entre o tamanho médio de palavra:"))
    ttr = float(input("Entre a relação Type-Token:"))
    hlr = float(input("Entre a Razão Hapax Legomana:"))
    sal = float(input("Entre o tamanho médio de sentença:"))
    sac = float(input("Entre a complexidade média da sentença:"))
    pal = float(input("Entre o tamanho medio de frase:"))

    return [wal, ttr, hlr, sal, sac, pal]


def le_textos():
    #'''A funcao le todos os textos a serem comparados e devolve uma lista contendo cada texto como um elemento'''
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")

    return textos


def separa_sentencas(texto):
    #'''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas


def separa_frases(sentenca):
    #'''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
    return re.split(r'[,:;]+', sentenca)


def separa_palavras(frase):
    #'''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
    return frase.split()


def n_palavras_unicas(lista_palavras):
    #'''Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez'''
    #'''Amiga do separador de palavras
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas


def n_palavras_diferentes(lista_palavras):
    #'''Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas'''
    #'''Amiga do separador de palavras
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)


def media_caracteres_palavras(texto):
    #'''Média simples do número de caracteres por palavra.'''
    soma = 0
    qtd_palavras = 0
    for sentenca in separa_sentencas(texto):
        for frase in separa_frases(sentenca):
            for palavra in separa_palavras(frase):
                soma += len(palavra)
                qtd_palavras += 1
    return soma / qtd_palavras
    

def type_token(texto):
    #"""Número de palavras diferentes utilizadas em um texto divididas pelo total de palavras.'''  
    qtd_palavras = 0
    lista_palavras = []
    for sentenca in separa_sentencas(texto):
        for frase in separa_frases(sentenca):
            for palavra in separa_palavras(frase):
                qtd_palavras += 1
                if palavra not in lista_palavras:
                    lista_palavras.append(palavra)
    return n_palavras_diferentes(lista_palavras) / qtd_palavras
    
    
def hapax_legomana(texto):
    #'''Número de palavras utilizadas uma única vez dividido pelo número total de palavras.'''
    qtd_palavras = 0
    lista_palavras = []
    for sentenca in separa_sentencas(texto):
        for frase in separa_frases(sentenca):
            for palavra in separa_palavras(frase):
                qtd_palavras += 1
                lista_palavras.append(palavra)
    return n_palavras_unicas(lista_palavras) / qtd_palavras


def media_caracteres_sentenca(texto):
    #'''Média simples do número de caracteres por sentença.'''
    soma = 0
    for item in separa_sentencas(texto):
        soma += len(item)
    return soma / len(separa_sentencas(texto))
    
    
def complexidade(texto):
    #'''Média simples do número de frases por sentença.'''  
    soma = 0
    for item in separa_sentencas(texto):
        soma += len(separa_frases(item))
    return soma / len(separa_sentencas(texto))


def media_caracteres_frase(texto):
    #'''Média simples do número de caracteres por frase.'''
    soma = 0
    qtd_frases = 0
    for sentenca in separa_sentencas(texto):
        for frase in separa_frases(sentenca):
            soma += len(frase)
            qtd_frases += 1
    return soma / qtd_frases

def calcula_assinatura(texto):
    #'''Essa funcao recebe um texto e deve devolver a assinatura do texto.'''
    wal = media_caracteres_palavras(texto)
    ttr = type_token(texto)
    hlr = hapax_legomana(texto)
    sal = media_caracteres_sentenca(texto)
    sac = complexidade(texto)
    pal = media_caracteres_frase(texto)
    
    return [wal, ttr, hlr, sal, sac, pal]

    
def compara_assinatura(as_a, as_b):
    #''' Essa funcao recebe duas assinaturas de texto e deve devolver o grau de similaridade nas assinaturas.'''
    soma_diferencas = 0
    for i in range(6):
        soma_diferencas += abs((as_a)[i] - (as_b)[i])
    res = soma_diferencas / 6
    return res
    

def avalia_textos(textos, ass_cp):
    #'''Essa funcao recebe uma lista de textos e uma assinatura ass_cp 
    #'''e deve devolver o numero (1 a n) do texto com maior probabilidade de ter sido infectado por COH-PIAH.'''
    coh_piah = 10000000
    infectado = 0
    for i, texto in enumerate(textos):
        as_a = calcula_assinatura(texto)
        comp = compara_assinatura(as_a, ass_cp)
        if comp < coh_piah:
            coh_piah = comp
            infectado = i + 1
    return infectado 