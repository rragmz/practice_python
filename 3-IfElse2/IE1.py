"""
Recibir un mes
si es Enero: "que comiences bien el año!!!."
si es Marzo: "a clases!!!."
si es Julio: "se vienen las vacaciones!!!."
si es Diciembre: "Felices fiesta!!!."""

month = input('Ingrese un mes del año: ')

while month.isnumeric():
    month = input('Ingrese un mes del año: ')   
else:
    month = month.lower()
    if month == 'enero':
        print(month.capitalize(),': Que comiences bien el año!!!')
    elif month == 'marzo':
        print(month.capitalize(),': A clases!!!')
    elif month == 'julio':
        print(month.capitalize(),': Se vienen las vacaciones!!!')
    elif month == 'diciembre':
        print(month.capitalize(),': Felices Fiestas!!!')

