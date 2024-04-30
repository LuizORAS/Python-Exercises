#IDLE

#1

#a
def ContatinhosApp(nome,telefone='',email='',instagram=''):
    """Criar lista de contatos baseado num suposto App"""
    novo_contato = []
    lista_de_tel = []
    while True:
        if telefone not in lista_de_tel:
            lista_de_tel.append(telefone)
            break
    loop = 0
    while loop<4:
        if nome not in novo_contato:
            novo_contato.append(nome)
            loop += 1
        if lista_de_tel not in novo_contato:
            novo_contato.append(lista_de_tel)
            loop += 1
        if email not in novo_contato:
            novo_contato.append(email)
            loop += 1
        if instagram not in novo_contato:
            novo_contato.append(instagram)
            loop += 1
    return novo_contato

#b
novo_contato = ContatinhosApp('Luiz','2455-0912','luiz@gmail.com','@luizlima')

def AtualizarContato(indice, info_nova):
    """Atualização do contato anterior"""
    if indice ==1:
        if info_nova in novo_contato[indice]:
            return False
        else:
            list(novo_contato)[indice].append(info_nova)
            return True
    else:
        novo_contato[indice] = info_nova
        return True


#2
def trinca_rna(valor_rna: str):
    """Bagulho do RNA"""
    mapeamento_rna = {
        "UUU":'Phe',
        "CUU":'Leu',
        "UUA":'Leu',
        "AAG": 'Lisina',
        "UCU": 'Ser',
        "UAU": 'Tyr',
        "CAA":'Gln'
    }
    trinca_1 = valor_rna[:3]
    trinca_2 = valor_rna[3:6]
    trinca_3 = valor_rna[6:]
    return f'{mapeamento_rna[trinca_1]}-{mapeamento_rna[trinca_2]}-{mapeamento_rna[trinca_3]}'


#MT

#1
def intercala(lista1, lista2):
    """Define uma função que dada duas listas gera uma terceira que se forma intercalando os elementos das duas primeiras listas"""
    lista3 =[]
    if len(lista1)==len(lista2):
        for i in range(len(lista1)):
            lista3.append(lista1[i])
            lista3.append(lista2[i])
    else:
        if len(lista1)>len(lista2):
                diff = len(lista1) - len(lista2)
                for i in range(len(lista2)):
                            lista3.append(lista1[i])
                            lista3.append(lista2[i])
                lista3 = lista3 + lista1[-diff:]
        else:
            if len(lista2)>len(lista1):
                diff = len(lista2) - len(lista1)
                for i in range(len(lista1)):
                            lista3.append(lista1[i])
                            lista3.append(lista2[i])
                lista3 = lista3 + lista2[-diff:]
    return lista3

#2
def pontos_por_time(jogos_total) -> dict:
    """Continuação da desgraça"""
    #LISTA DOS TIMES:
    time1 = jogos_total[0][0]
    time2 = jogos_total[0][1]
    #PLACAR JOGO DE IDA
    placar_ida = jogos_total[0][2]
    placar_time1_1a = placar_ida[0]
    placar_time2_1a = placar_ida[1]
    #QUANTIDADE DE PONTOS IDA
    pontos_time1_ida = 0
    pontos_time2_ida = 0
    #PLACAR JOGO DE VOLTA
    placar_volta = jogos_total[1][2]
    placar_time1_2a = placar_volta[1]
    placar_time2_2a = placar_volta[0]
    #QUANTIDADE DE PONTOS VOLTA    
    pontos_time1_volta = 0
    pontos_time2_volta = 0
    #TOTAL DE PONTOS
    ponto_total_time1 = 0
    ponto_total_time2 = 0
    #JOGO IDA
    if placar_time1_1a> placar_time2_1a:
        pontos_time1_ida += 3
    elif placar_time1_1a < placar_time2_1a:
        pontos_time2_ida += 3
    elif placar_time1_1a == placar_time2_1a:
        pontos_time1_ida += 1
        pontos_time2_ida += 1
    #JOGO VOLTA
    if placar_time1_2a> placar_time2_2a:
        pontos_time1_volta += 3
    elif placar_time1_2a < placar_time2_2a:
        pontos_time2_volta += 3
    elif placar_time1_2a == placar_time2_2a:
        pontos_time1_volta += 1
        pontos_time2_volta += 1
    #SOMATORIA DO PLACAR
    ponto_total_time1 = pontos_time1_ida + pontos_time1_volta
    ponto_total_time2 = pontos_time2_ida + pontos_time2_volta
    #PLACAR   
    placar_total = {time1: ponto_total_time1, time2: ponto_total_time2}
    return placar_total

#3
def colchao(medidas, H, L):
    """Ultima dessa desgraça"""
    med_a = medidas[0]
    med_b = medidas[1]
    med_c = medidas[2]
    if H > med_a or L > med_a:
        if H >= med_b or L >= med_b or H >= med_c or L >= med_c:
            return True
        else:
            return False
    else:
        return False
