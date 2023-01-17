""". Adivina el número (v 2.0): En esta oportunidad el juego evaluará tus aptitudes a partir de la cantidad de intentos, por lo cual se informará lo siguiente:
1° intento: “usted es un Psíquico”.
2° intento: “excelente percepción”.
3° intento: “Esto es suerte”.
4° intento: “Excelente técnica”.
5° intento: “usted está en la media”.
Desde 6 Intentos hasta 10:”falta técnica”
Más de 10 intentos: “afortunado en el amor!!”."""

import random
number = random.randint(1,101)
attemps = 0

def is_positive(arg):
    result = 1
    if not arg.isnumeric() or int(arg) < 0:
        result = 0
    return result 

def valid_number():
    number = input('Ingrese un número del 1 al 100: ')

    while not is_positive(number):
        number = input('Ingrese un número del 1 al 100: ')
    return int(number)

def valid_attemps(number):
    if number == 1:
        print('Usted es un psíquico!')
    elif number == 2:
        print("Excelente percepción")
    elif number == 3:
        print('Esto es suerte')
    elif number == 4:
        print('Excelente técnica')
    elif number == 5:
        print('Usted está en la media')
    elif number >= 6 and number <= 10:
        print('Falta técnica')
    else:
        print('Afortunado en el amoooorrr!!')

choice = valid_number()

while choice != number:
    if choice < number:
        print('Falta...')
    else:
        print('Te pasaste')
    attemps = attemps + 1
    choice = valid_number()
else:
    valid_attemps(attemps)
    print(f'Intentos: {attemps}')