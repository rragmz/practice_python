"""3. Piedra, Papel o Tijera (v 1.0):
Al comenzar el juego generaremos un número RANDOM del 1 al 3 para la selección de la máquina, siendo 1 para “piedra”, el 2 para “papel” y 3 para “tijera”.
El jugador seleccionará una imagen correspondiente a su opción y le informaremos si ganó, empató o perdió"""
import random

game = random.randint(1,4)

def is_positive(arg):
    result = 1
    if not arg.isnumeric() or int(arg) < 0:
        result = 0
    return result 

def valid_number_in_range(message, init, final):
    number = input(f'{message}')

    while not is_positive(number) or not(int(number) >= init and int(number) <= final):
        number = input(f'{message}')
    return int(number)

# 1 -> Piedra
# 2 -> Papel2
# 3 -> Tijera 

def game_message(result):
    if result == -1:
        print('Perdiste!')
    elif result == 0:
        print('Empataron!')
    else:
        print('Ganaste!')

def scissor_paper_rock():
    choice = valid_number_in_range('1. Piedra\n2. Papel\n3. Tijera: ', 1, 3)
    if(game == 1):
        if(choice == 1):
            game_message(0)
        elif(choice == 2):
             game_message(1)
        else:
             game_message(-1)
    elif(game == 2):
        if(choice == 1):
             game_message(-1)
        elif(choice == 2):
             game_message(0)
        else:
             game_message(1)
    else:
        if(choice == 1):
            game_message(1)
        elif(choice == 2):
            game_message(-1)
        else:
            game_message(0)

scissor_paper_rock()