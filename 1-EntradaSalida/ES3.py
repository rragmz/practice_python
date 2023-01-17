"""Recibir un número mayor a 1000 y mostrarlo con un 25% de descuento"""
value = input('Ingrese un número mayor o igual a 1000: ')

while not value.isnumeric() or int(value) < 1000 :
    value = input('Ingrese un número mayor o igual a 1000: ')
else:
    value = int(value)
    value = value - (value) * 25 / 100
    print('El valor con descuento aplicado es: ', value)

    
