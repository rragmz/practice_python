"""Adivina el número (v 1.0): Al comenzar el juego generamos un número secreto del 1 al 100, en la pantalla del juego dispondremos de un cuadro de texto para ingresar un número y un botón “Verificar”, si el número ingresado es el mismo que el número secreto se dará por terminado el juego con un mensaje similar a este:
“Usted es un ganador!!! y en solo X intentos”. de no ser igual se debe informar si “falta…” para llegar al número secreto o si “se pasó…” del número secreto."""
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


choice = valid_number()

while choice != number:
    if choice < number:
        print('Falta...')
    else:
        print('Te pasaste')
    attemps = attemps + 1
    choice = valid_number()
else:
    print(f'Ganaste! Solo en {attemps}')

    

