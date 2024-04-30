#IDLE

#1
def remover_numero(contato, telefone):
    """Atualizar sapoha"""
    if telefone in contato[1]:
        contato[1].remove(telefone)
        return True
    else:
        return False

#2
def tabela_de_pontos(tabela):
    """Tabela de futsoccer rsrsrs"""
    tabela_l = [list(tabela), max(dict.values(tabela)), sum(dict.values(tabela))/len(dict.keys(tabela))]
    return f'Os times são {tabela_l[0]}, o campeão tem {tabela_l[1]} pontos e a média de pontos é {tabela_l[2]}.'

#MT

#1
def quant_palavras(frase):
    """1o DO MT"""
    qnt_de_palavra = len(frase.split())
    return qnt_de_palavra

#2
#EU SOU BOM PRA CARALHO VAI TOMAR NO CU, PORRA. CARALHO VAI SE FUDER
def conta_frases(frase):
    sentencas = frase.split()
    contagem = 0
    simbolos = ['.', '!', '?', '...']
    for palavras in sentencas:
        for simbolo in simbolos:
            if simbolo in palavras:
                if '...' in palavras and simbolo == '.':
                    contagem += 0
                else:
                    contagem += 1
    return contagem

#3
def retira_pontuacao(frase):
    """3o do MT, VEM PAPAI"""
    sentencas = frase.split()
    caracteres = ['.', '!', '?', '...', ',', ':', ';', '–','-']
    for i in range(len(sentencas)):
        for caractere in caracteres:
            if caractere in sentencas[i]:
                mudanca = sentencas[i].replace(caractere, ' ')
                sentencas[i] = mudanca
    nova_frase = ' '.join(sentencas)
    return nova_frase

#4
def inverte(frase):
    nova_frase = []
    frase_nova = retira_pontuacao(frase)
    frase_splitada = frase_nova.split()
    for i in range(len(frase_splitada)+1):
            if i == 0:
                pass
            else:
                nova_frase.append(frase_splitada[-i])
    frase_final = ' '.join(nova_frase)
    return frase_final.lower()


#5
def insere(lista_ord, num):
    """5a DESSA PORRA"""
    num_int = int(num)
    lista_ord.append(num_int)
    lista_ord.sort()
    return lista_ord

#6
def maiores(lista_num, num):
    """6o DESSA PORRA"""
    lista_de_maior = []
    for i in lista_num:
        if i > num:
            lista_de_maior.append(i)
    lista_de_maior.sort()
    return lista_de_maior

#7
def acima_da_media(lista_de_nota):
    """ULTIMA DESSA PORRA"""
    media = sum(lista_de_nota)/len(lista_de_nota)
    resultado = maiores(lista_de_nota, media)
    return resultado
