"""Al ingresar una edad debemos informar si la persona es mayor de edad (mas de 18 años) o adolescente (entre 13 y 17 años) o niño (menor a 13 años)."""
age = input('Ingrese su edad: ')

while not age.isnumeric() or int(age) < 0 or int(age) > 110:
    age = input('Ingrese su edad: ')

else:
    age = int(age)
    if age >= 18:
        print('Sos mayor de edad')
    elif age >= 13 and age <= 17:
        print('Sos adolescente')
    else:
        print('Sos niño/a')