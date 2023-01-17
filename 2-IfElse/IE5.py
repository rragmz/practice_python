"""Al ingresar una edad solo debemos informar si la persona NO es adolescente."""
age = input('Ingrese su edad: ')

while not age.isnumeric() or int(age) < 0 or int(age) > 110:
    age = input('Ingrese su edad: ')
else:
    age = int(age)
    if age < 13 or age > 17:
        print('No sos adolescente')
