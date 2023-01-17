"""Recibir un número que represente la edad de alguien y si es 15 mostrar 'niña bonita'"""
age = input('Ingrese su edad: ')

while not age.isnumeric() or int(age) < 0 or int(age) > 110:
    age = input('Ingrese su edad: ')
else:
    age = int(age)
    if age == 15:
        print('Niña Bonita')
