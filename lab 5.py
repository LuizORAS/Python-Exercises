#IDLE

#1
def find_elem(iterable, elem):
    """AI AI MINHA BUCETINHA"""
    count_elem = 0
    for i in iterable:
        if i == elem:
            count_elem +=1
    return count_elem

#2
def find_lim_elem(iterable, ini: int, fim: int, elem):
    """QUANDO O NATHAN ME OLHA EU FICO-"""
    interv_iter = iterable[ini:fim+1]
    return find_elem(interv_iter, elem)

#3
def atualiza_mascara(palavra_secreta, masc_atual, letra):
    """EU FICO TODA MOLHADINHA"""
    posic_certa = []
    if letra in palavra_secreta:
        for a in range(len(palavra_secreta)):
            if palavra_secreta[a]==letra:
                posic_certa.append(a)
        for i in posic_certa:
            masc_atual[i] = letra
        return masc_atual
    else:
        return masc_atual

#4
#não.

#MT

#1
def freq_palavra(frase: str):
    """COLDPLAY - YELLOW"""
    frase = frase.split()
    conta_frase = []
    novo_dict = {}
    for i in range(len(frase)):
        conta_frase.append(frase.count(frase[i]))
        novo_dict.update({frase[i]:conta_frase[i]})
    return novo_dict

#2
def total(lista_de_compras, dict_precos):
    """DONT ANGER - OASIS"""
    valor_total = []
    for i in lista_de_compras:
        if i in dict_precos:
            valor_total.append(dict_precos[i])
    return round(sum(valor_total),2)

#3
def lingua_p(palavra):
	vogais = ['a', 'e', 'i', 'o', 'u', 'á', 'é', 'í', 'ó', 'ú', 'ã', 'õ', 'â','A', 'E', 'I', 'O', 'U', 'Á', 'É', 'Í', 'Ó', 'Ú', 'Ã', 'Õ', 'Â']
	new = []
	for i in palavra:
		if i in vogais:
			new.append(i)
			new.append('p'+i)
		else:
			new.append(i)
	new = ''.join(new).lower()
	return new

#4
def qtd_divisores(num):
    """CHAMPAGNE SUPERNOVA - OASIS"""
    cont = 0 
    for i in range(num+1):
        if i == 0:
            pass
        elif num % i == 0:
            cont += 1
    return cont

#5
def primo(num):
    cont = 0
    for i in range(num+1):
        if i == 0:
            pass
        elif num % i == 0:
            cont += 1
    return bool(cont == 2)

#6
def soma_h(n):
    """WONDERWALL - OASIS """
    lista_de_sum = []
    for i in range(1,n+1):
        lista_de_sum.append(i**-1)
    return round(sum(lista_de_sum),2)


