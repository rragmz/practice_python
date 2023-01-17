"""El departamento de NUMEROS ESPECIALES del instituto matemático FonteCristo nos está pidiendo una aplicación que verifique las distintas cualidades de los números.
Para cada una de estas acciones debemos realizar la lógica para verificar las cualidades pedidas:
A. Se pedirán un número positivo y se mostrará la cantidad de números pares desde el número ingresado hasta el cero.
B. Se pedirán un número positivo y se mostrará la cantidad de números impares desde el número ingresado hasta el cero.
C. Se pedirán un número positivo y se mostrará la cantidad de números divisibles de este número que se encuentran desde el 1 al 100.
D. Se pedirán un número positivo y se mostrará si el número es un número primo o no.
E. Se pedirán un número positivo y se mostrará la cantidad de números Primos desde el número ingresado hasta el cero."""

import sympy

def num_pos(number):
    result = 1
    if not number.isnumeric() or int(number) < 0:
        result = 0
    else:
        return result

def show_even(number):
    number = int(number)
    array_even = []
    for x in range(number,-1,-1):
        if x % 2 == 0:
          array_even.append(x)
    return array_even

def show_odd(number):
    number = int(number)
    array_odd = []
    for x in range(number,-1,-1):
        if x % 2 != 0:
            array_odd.append(x)
    return array_odd

def divider(number):
    number = int(number)
    array = []
    for x in range(1, 100):
        if number % x == 0:
            array.append(x)
    return array

def prime_number(number):
    number = int(number)
    result = 0
    if sympy.isprime(number):
        result = 1
    return result

def quantity_primes(number):
    number = int(number)
    array = []
    for x in range(number, 0, -1):
        if sympy.isprime(x):
            array.append(x)
    return array

number = input('Ingrese un número positivo y entero: ')
while not num_pos(number):
    number = input('Ingrese un número positivo y entero: ')
else:
    int(number)

#Mostrará la cantidad de números pares desde el número ingresado hasta el cero.
print(f'Los números pares desde {number} hasta 0 son: {show_even(number)}')

#Mostrará la cantidad de números impares desde el número ingresado hasta el cero.
print(f'Los números impares desde {number} hasta 0 son: {show_odd(number)}')

#Mostrará la cantidad de números divisibles de ese número del 1 al 100.
print(f'Los números divisibles de {number} del 1 al 100 son: {divider(number)}')

#Mostrará si ese es un número primo o no
if prime_number(number):
    print(f'El número {number} es primo')
else:
    print(f'El número {number} NO es primo')

#Mostrará la cantidad de número primos que hay desde ese número al 0
print(f'Los número primos desde {number} hasta 0 son: {quantity_primes(number)}')
