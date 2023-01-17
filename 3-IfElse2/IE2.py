"""Recibir un mes.
si estamos en Invierno: "Abrigate que hace frio."
si aún no llego el Invierno: "Falta para el invierno."
si ya paso el Invierno: "Ya pasamos el frio, ahora calor!!!."
ACLARAcIÓN: tomamos a Julio y Agosto como los meses de Invierno."""

month = input('Ingrese un mes del año: ')

while month.isnumeric():
    month = input('Ingrese un mes del año: ')   
else:
    month = month.lower()
    if month == 'julio' or month == 'agosto':
        print(month.capitalize(),': Abrigate que hace frío!')
    elif month == 'septiembre' or month == 'octubre' or month == 'noviembre' or month == 'diciembre' or month == 'enero' or month == 'febrero':
        print(month.capitalize(),': Ya pasamos el frío, ahora el calor!!!')
    elif month == 'marzo' or month == 'abril' or month == 'mayo' or month == 'junio':
        print(month.capitalize(),': Falta para el invierno')
    else:
       print('Ingresó un mes inválido')

