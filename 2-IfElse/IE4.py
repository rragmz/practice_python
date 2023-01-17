"""Al ingresar una edad debemos informar si la persona es adolescente, edad entre 13 y 17 años (inclusive) ."""
age = input('Ingrese su edad: ')

while not age.isnumeric() or int(age) < 0 or int(age) > 110:
    age = input('Ingrese su edad: ')
else:
    age = int(age)
    if age >= 13 and age <= 17:
        print('Sos adolescente')
