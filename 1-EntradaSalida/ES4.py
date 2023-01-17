"""Ingresar nombre y edad e imprimir por consola: 'Tu nombre es x y tu edad es y años'"""

ingreso = input('Ingrese nombre y edad: ')
partes = ingreso.split()
edad = partes.pop()
nombre = ' '.join(partes)

print(f'Tu nombre es {nombre} y tu edad {edad} años')