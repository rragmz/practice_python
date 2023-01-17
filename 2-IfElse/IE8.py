"""Al ingresar una edad menor a 18 años y un estado civil distinto a "Soltero", NO HACER NADA,
pero si no es asi, y es soltero y no es menor, mostrar el siguiente mensaje: 'Es soltero y no es menor.'"""


age = input('Ingrese su edad: ')

while not age.isnumeric() or int(age) < 0 or int(age) > 110:
    age = input('Ingrese su edad: ')

else:
    marital_status = input('Ingrese su estado civil: ')

    while marital_status.isnumeric():
        marital_status = input('Ingrese su estado civil: ')

    else:
        age = int(age)
        marital_status=marital_status.lower()

        if age >= 18 and marital_status == 'soltero':
            print('Es soltero y no es menor.')