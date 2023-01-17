# Informar si el numero es PRIMO o no
import sympy
lim = int(input('Choice a number: '))

for x in range(1, lim + 1):
    if sympy.isprime(x):
        print(x)