#IDLE
import random

#1
def dados():
    """1a desse cu-chan"""
    contagem = 0
    while True:
        a = random.randint(1,6)
        print(f' dado1 = {a}')
        b = random.randint(1,6)
        print(f' dado2 = {b}')
        contagem +=1
        if a == b:
            break
    return f'foram jogados {contagem} vezes até que saissem repetidos'

#2
def achar_dados(lista_contatos,nome):
    """EU QUERO SABER QUEM É QUE FODE, QUEM FODE NESSA PORRA"""
    lista_de_busca = []
    b = lambda a: a.lower()
    for vezes in range(len(lista_contatos)):
        for contato in lista_contatos:
            for dado in contato:
                if isinstance(dado, str):
                        if b(nome) in b(dado):
                            if contato in lista_de_busca:
                                pass
                            elif contato not in lista_de_busca:
                                lista_de_busca.append(contato)
                elif isinstance(dado, list):
                    for num in dado:
                        if nome in dado:
                            if contato in lista_de_busca:
                                pass
                            elif contato not in lista_de_busca:
                                lista_de_busca.append(contato)

    return lista_de_busca

#MT 

#1
def filtraMultiplos(lista_de_num, num):
    """1O DO MT ; O FLAMENGO NÃO TAVA BEM"""
    lista_de_divisiveis = []
    for i in lista_de_num:
        if i%num==0:
            lista_de_divisiveis.append(i)
    return lista_de_divisiveis

#2
# REFAZER ESSA MERDA POR ULTIMO DEPOIS DE COMEÇAR A FAZER ; QUESTÃO FILHA DA PUTA QUE VC TALVEZ NÃO LEMBRE QUE FEZ E VAI PASSAR RAIVA MESMO ASSIM
# DICA, EU USEI APENAS FOR LOOP. TENTE USAR WHILE, LAMBDA E ETC... FOR LOOP VAI TE FUDER GOSTOSO.
def uppCons(frase):
    nova_frase = ""
    for letra in frase:
        if letra in ['a', 'e', 'i', 'o', 'u', 'á', 'é', 'í', 'ó', 'ú', 'ã', 'õ', 'â'] or letra in ['A', 'E', 'I', 'O', 'U', 'Á', 'É', 'Í', 'Ó', 'Ú', 'Ã', 'Õ', 'Â']:
            nova_frase += letra
        else:
            nova_frase += letra.upper()
    return nova_frase


#3
def posLetra(string,letra,ocorrencia):
    """ULTIMA GRAÇAS A DEUS"""
    #O '-1' ABAIXO SE REFERE AO FATO DE QUE O PYTHON COMEÇA NO 0 E NÃO NO 1. // ex: ' a = "charlie" ; a[0] = c ' AO INVÉS DE: 'a[1] = c' POR ISSO O '-1'
    contagem_string = -1
    contagem_da_letra = 0
    if string.count(letra)<ocorrencia:
        return -1
    else:
        for i in string:
            if i != letra:
                contagem_string += 1
            elif i == letra:
                contagem_string += 1
                contagem_da_letra +=1
                if contagem_da_letra == ocorrencia:
                    posic_certa = contagem_string
    return posic_certa

#4
def repetidos(lista_num):
    contagem = 0
    for i in range(len(lista_num)):
        if i == 0:
            pass
        else:
            if lista_num[i] == lista_num[i-1]:
                contagem +=1
    return contagem

#5
def fatorial(num):
    fatr = 1
    if isinstance(num, int):
        if num>0:
            for i in range(2,num+1):
                fatr *= i
        elif num==0:
            return fatr
        else:
            return 'Numero não é positivo'
    else:
        return 'Valor não é inteiro ou não é um numero'
    return fatr

#6
def faltante(lista_l):
    """QUESTÃO DA OBI"""
    x = len(lista_l)
    x = x+1
    x_inicial = 1
    copia_l = []
    lista_de_faltante = []
    lista_l.sort()
    for i in range(x_inicial,x+1):
        copia_l.append(i)   
    for y in copia_l:
        if y not in lista_l:
            lista_de_faltante.append(y)
    if len(lista_de_faltante)==1:
        return lista_de_faltante[0]
    else:
        return lista_de_faltante



