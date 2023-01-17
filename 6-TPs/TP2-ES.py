"""Para el departamento de Construcción:
A. mostrar la cantidad de alambre a comprar si se ingresara el largo y el ancho de un terreno rectangular y se debe alambra con tres hilos de alambre.
B. mostrar la cantidad de alambre a comprar si se ingresara el radio de un terreno circular y se debe alambra con tres hilos de alambre.
C. Para hacer un contrapiso de 1m x 1m se necesitan 2 bolsas de cemento y 3 de cal, debemos mostrar cuantas bolsas se necesitan de cada uno para las medidas del terreno rectangular."""

#Consulta al usuario
large = input('Ingrese el largo del terreno o 0: ')
while not large.isnumeric() or float(large) < 0:
    large = input('Ingrese el largo del terreno o 0: ')

width = input('Ingrese el ancho del terreno o 0: ')
while not width.isnumeric() or float(width) < 0:
    width = input('Ingrese el ancho del terreno o 0: ')

radio = input('Ingrese el radio del terreno o 0: ')
while not radio.isnumeric() or float(radio) < 0:
    radio = input('Ingrese el radio del terreno o 0: ')

action = input('Qué desea realizar (ingrese el número correspondiente)\n1. Rectángulo de alambre\n2. Círculo de alambre\n3. Materiales contrapiso: ')
while not action.isnumeric() or (int(action) != 1 and int(action) != 2 and int(action) != 3):
    action = input('Qué desea realizar (ingrese el número correspondiente)\n1. Rectángulo de alambre\n2. Círculo de alambre\n3. Materiales contrapiso: ')

else:
    action = int(action)
    if action == 1:
            large = float(large)
            width = float(width)
            amount_wire = format((large * 2 + width * 2) * 3, '.2f')
            print(f'Necesitarás {amount_wire} metros de alambre')

    elif action == 2:
        radio = float(radio)
        amount_wire = format((2 * 3.1416 * radio) * 3, '.2f')
        print(f'Necesitarás {amount_wire} metros de alambre')

    elif action == 3:
        large = float(large)
        width = float(width)
        perimeter = large*2 + width*2
        amount_cement = 2*perimeter
        amount_lime = 3*perimeter
        print(f'Necesitarás {amount_cement} bolsas de cemento y {amount_lime} bolsas de cal')