"""Tomar dos números y mostrar el resultado de la operación que elija el usuario"""
import math

num1 = int(input('Ingrese un numero: '))
num2= int(input('Ingrese otro número: '))
operacion = input('Elija la letra que corresponde a qué operación quiere realizar: \na. Suma\nb. Resta\nc. Multiplicación\nd. División: ').lower()

if operacion == 'a':
    resultado = num1+num2
elif operacion == 'b':
    resultado = num1-num2
elif operacion == 'c':
    resultado = num1*num2
elif operacion == 'd':
    resultado= format((num1/num2), ".2f")
else:
    resultado = 'La operación que intentas realizar no existe'

print('El resultado es: ', resultado)