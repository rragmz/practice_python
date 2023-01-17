"""Recibir un mes
al seleccionar un mes informar.
si tiene 28 días.
si tiene 30 días.
si tiene 31 días."""

month = input('Ingrese un mes del año: ')

while month.isnumeric():
    month = input('Ingrese un mes del año: ')   
else:
    month = month.lower()
    if month == 'enero' or month == 'marzo' or month == 'mayo' or month == 'julio' or month == 'agosto' or month == 'octubre' or month == 'diciembre':
        print(f'{month.capitalize()} tiene 31 días')
    elif month == 'abril' or month == 'junio' or month == 'septiembre' or month == 'noviembre':
        print(f'{month.capitalize()} tiene 30 días')
    elif month == 'febrero':
        print(f'{month.capitalize()} tiene 28 días o 29 si es año bisiesto')
    else:
        print('Ese mes no existe')