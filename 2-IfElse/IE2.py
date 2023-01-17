"""Al ingresar una edad debemos informar solo si la persona es mayor de edad"""
age = input('Ingrese su edad: ')

while not age.isnumeric() or int(age) < 0 or int(age) > 110:
    age = input('Ingrese su edad: ')
else:
    age = int(age)
    if age >= 18:
        print('Sos mayor de edad')
