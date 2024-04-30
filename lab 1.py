# 1
from ast import For
from itertools import count
from re import I, S
from types import new_class


def SIGA(aluno, nota1, nota2, nota3) -> tuple:
    """Nota dos alunos"""
    média = ((nota1+nota2+nota3)/3)
    if média > 7:
        return f'{aluno}, {round(média,1)}, Aprovado, Parabéns!'
    elif 5 <= média < 7:
        return f'{aluno}, {round(média,1)}, Aprovado.'
    else:
        return f'{aluno}, {round(média,1)}, Reprovado.'


# 2
def zodiaco_chines(ano_de_nasc: int):
    """Ver zodiaco chines"""
    zodiaco = {
        0: 'Macaco',
        1: 'Galo',
        2: 'Cao',
        3: 'Porco',
        4: 'Rato',
        5: 'Boi',
        6: 'Tigre',
        7: 'Coelho',
        8: 'Dragao',
        9: 'Serpente',
        10: 'Cavalo',
        11: 'Carneiro'}
    ano_do_zodiaco = ano_de_nasc % 12
    return zodiaco[ano_do_zodiaco]


# 3
def ddd_br(telefone):
    """Telefone brasil"""
    if int(len(telefone)) not in [8, 10, 9, 11]:
        return tuple()
    else:
        for i in telefone:
            if i not in str([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]):
                return tuple()
        if int(len(telefone)) in [8, 9]:
            return (' ', telefone)
        elif int(len(telefone)) in [10, 11]:
            ddd = telefone[0]+telefone[1]
            return (ddd, telefone[2:])

# 4


def formato_data(data: str) -> str:
    """MUST ENTER WITH THE FOLLOWING FORMATS:
    DD/MM/YY OR MM/DD/YY OR YY/MM/DD"""
    dia = int(data[:2])
    mes = int(data[3:5])
    ano = int(data[6:8])
    if str(dia)[0] and str(dia)[1] not in ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9'):
        return tuple()
    if str(mes)[0] and str(mes)[1] not in ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9'):
        return tuple()
    if str(ano)[0] and str(ano)[1] not in ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9'):
        return tuple()
    for i in data:
        if i not in str([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, '/']):
            return tuple()
    for i in data:
        if i in ['-', '[', ']']:
            return tuple()
    if int(list(data).count('/')) not in [2]:
        return tuple()
    elif len(data) != 8:
        return tuple()
    else:
        if dia <= 12 and mes <= 12 and ano <= 12:
            return ('dd/mm/yy', 'mm/dd/yy', 'yy/mm/dd')
        elif dia <= 31 and mes <= 12 and ano <= 31:
            return ('dd/mm/yy', 'yy/mm/dd')
        elif dia <= 12 and mes <= 12 and ano <= 31:
            return ('yy/mm/dd', 'mm/dd/yy')
        elif dia <= 12 and mes <= 12:
            return ('dd/mm/yy', 'mm/dd/yy')
        elif dia <= 31 and mes <= 12:
            return ('dd/mm/yy')
        elif mes <= 12 and ano <= 31:
            return ('yy/mm/dd')
        elif dia <= 12 and mes <= 31:
            return ('mm/dd/yy')
        else:
            return tuple()

# MT

# 1


def concatenacao(a: str, b: str):
    """CONCATENAÇÃO FREESTYLE"""
    new_conc = ''
    conc_count = 0

    while conc_count < 1:
        new_conc += a
        conc_count += 1
    while conc_count < 3:
        new_conc += b
        conc_count += 1
    while conc_count < 4:
        new_conc += a
        conc_count += 1
    return new_conc

# 2


def substitui(s, x, i):
    s = list(s)
    s[i] = str(x)
    s = ''.join(s)
    return s
    # errei essa - peguei cola do MT

# 3


def hashtag(s):
    """ Hashtag é uma função que recebe uma string e insere um "#" no inicio. meio e fim"""
    l = len(s)//2
    return "#" + s[:l] + "#" + s[l:] + "#"
    # peguei cola tb - mas fui burro tb, muito fácil

# 4
def filtra_pares(lista_tupla: tuple):
    """filtrar pares"""
    nova_lista = []
    for i in lista_tupla:
        if i % 2 == 0:
            nova_lista.append(i)
    nova_tupla = tuple(nova_lista)
    return nova_tupla

#5
def colisao(reta_t: tuple, reta_z: tuple):
    """ verificar colisao """
    t1 = reta_t[:2]
    t2 = reta_t[2:]
    z1 = reta_z[:2]
    z2 = reta_z[2:]
    x_maior_1 = t2[0]
    x_maior_2 = z2[0]
    x_menor_1 = t1[0]
    x_menor_2 = z1[0]
    y_maior_1 = t2[1]
    y_maior_2 = z2[1]
    y_menor_1 = t1[1]
    y_menor_2 = z1[1]

    #estudar colisoes com esses vértices acima - usar mentalidade menor, maior // maior, menor => para detectar colisoes, quebre a cabeça!
    if x_menor_1 > x_maior_2 or y_menor_1 > y_maior_2 or x_menor_2 > x_maior_1 or y_menor_2 > y_maior_1:
        return False
    else:
        return True
