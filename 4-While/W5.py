#Pedir el sexo. F/M. Validar

gender = input('Ingrese su sexo (F: femenino/M: masculino): ')

while gender.isnumeric() or len(gender) > 1 or (gender.capitalize() != 'F' and gender.capitalize() != 'M'):
    gender = input('Ingrese su sexo (F: femenino/M: masculino): ')
else:
    gender = gender.capitalize()
    if gender == 'F':
        print('Usted es mujer')
    elif gender == 'M':
        print('Usted es hombre')
