import random

### JOGOS USANDO RANDOM ###

# JOGO DA TENTATIVA - NUMERO ALEATORIO - SEM No DE TENTATIVAS
def acertar_numero():
    numero = random.randint(1, 10)
    while True:
        numero_chutado = int(input("> "))
        if numero_chutado == numero:
            print("Você ganhou!")
            break
        if numero_chutado < numero:
            print("O numero é maior")
        elif numero_chutado > numero:
            print("O numero é menor")
        else:
            print("Erro, repita por favor.")


# JOGO DA TENTATIVA - NUMERO ALEATORIO - COM No DE TENTATIVAS
def acertar_numero():
    numero = random.randint(1, 10)
    tentativa = 0
    while tentativa < 4:
        numero_chutado = int(input("> "))
        tentativa += 1
        if tentativa >= 4:
            print("Você perdeu!")
        elif numero_chutado == numero:
            print("Você ganhou!")
            break
        elif numero_chutado < numero:
            print("O numero é maior")
        elif numero_chutado > numero:
            print("O numero é menor")


# JOGO DA TENTATIVA - NUMERO ALEATORIO - INFINITO
def acertar_numero():
    numero = random.randint(1, 10)
    while True:
        numero_chutado = int(input("> "))
        if numero_chutado == numero:
            print("Você ganhou!")
            numero = random.randint(1, 10)
        elif numero_chutado < numero:
            print("O numero é maior")
        elif numero_chutado > numero:
            print("O numero é menor")
        else:
            print("Erro, repita por favor.")