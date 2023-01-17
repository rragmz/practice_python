"""Recibir un número que respresentará el sueldo y mostrarlo con un 10% de aumento"""
import math
sueldo = input('Ingrese su sueldo: ')

while not sueldo.isnumeric():
    sueldo = input('Ingrese su sueldo: ')
else:
    sueldo = int(sueldo)
    sueldoConAumento = sueldo * 10 / 100 + sueldo
    print('Su sueldo con 10% de aumento es: ', sueldoConAumento)

    
