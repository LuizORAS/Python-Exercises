# 1 - JOGO DA CASA
def house_price(buyer):
    house = 1000000
    if buyer == 'has good credit':
        return house*0.10
    else:
        return house*0.20

print(house_price('has good credit'))
print(house_price('has bad credit'))

print((f"it is ${house_price('has good credit')}"))

# 2 - VERIFICADOR DE TAMANHO DE NOME

def name_len(name):
    if len(name) < 3:
        return 'name must be 3 characters long'
    elif len(name) > 50:
        return 'name can be a maximum 50 characters long'
    else:
        return 'name looks good!'


print(name_len('gu'))
print(name_len('robertaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaba'))
print(name_len('thiago'))

# 3 - CONVERSOR DE PESO

def weight_converter():
    weight_value = input('Weight:')
    weight_option = input('(L)lbs or (K)kgs:')

    if weight_option.upper() == 'L':

        return print(f' Your weight in kilograms is {int(weight_value)*0.45}')

    if weight_option.upper() == 'K':
        return print(f'Your weight in pounds is {int(weight_value)/0.45}')

    else:
        return print('invalid option')


print(weight_converter())

# 4 - WHILE LOOP TRAINING
    # JOGO DO CARRO


def car_break():
    print("start - to start the car")
    print("stop - to stop the car")
    print("quit - to exit")

    started = False

    while True:
        option = str(input('> '))

        if option in ['Quit', 'quit']:
            break
        elif option in ['Start', 'start']:
            if started:
                print('The car already started!')
            else:
                started = True
                print('the car is moving...')
        elif option in ['Stop', 'stop']:
            if not started:
                print('The car already stopped!')
            else:
                started = False
                print('the car has stopped')
        else:
            print('Invalid option, try again.')


print(car_break())

# 5 - FOR LOOP TRAINING

# LISTA MERCADO, FOR LOOPS
def list_cost():
    prices = [10, 5.50, 12, 2.50, 45]

    total_price = 0

    for price in prices:
        total_price += price

    print(f'Total is ${total_price}')

print(list_cost())


# JOGO DAS LETRAS
def type_letter():

    numbers = [5, 2, 5, 2, 2]

    for number in numbers:
        output = ''
        for x_count in range(number):
            output += 'x'
        print(output)

print(type_letter())

# 7 - JOGO DO TELEFONE

def inserir_num():
    celular = input("Phone: ")
    teclado_de_numeros = {
        "1": "Um",
        "2": "Dois",
        "3": "Três",
        "4": "Quatro",
        "5": "Cinco",
        "6": "Seis",
        "7": "Sete",
        "8": "Oito",
        "9": "Nove",
        "0": "Zero"}
    resultado_da_discagem = ""
    for numero_inserido in celular:
        resultado_da_discagem += teclado_de_numeros.get(
            numero_inserido, "!") + " "
    return (resultado_da_discagem)

print(inserir_num())