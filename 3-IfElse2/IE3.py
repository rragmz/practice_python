"""Recibir un mes.
si es Febrero: " Este mes no tiene más de 29 días."
si NO es Febrero: "Este mes tiene 30 o más días"""

month = input('Ingrese un mes del año: ')

while month.isnumeric():
    month = input('Ingrese un mes del año: ')   
else:
    month = month.lower()
    if month == 'febrero':
        print('Este mes no tiene más de 29 días')
    else:
        print('Este mes tiene 30 días o más')