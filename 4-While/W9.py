# Pedir números hasta que el usuario quiera, mostrar el número máximo y el número mínimo ingresado.

answer = 'y'
i = 0

while answer == 'y':
    number = int(input('Ingrese un número: '))
    if i == 0:
        min_number = number
        max_number = number
    else:
        if number < min_number:
            min_number = number
        elif number > max_number:
            max_number = number
    answer = input('Desea seguir ingresando números? y/n: ').lower()
    i = i + 1
else:
    print(f'El número mínimo fue: {min_number}\nEl máximo: {max_number}')