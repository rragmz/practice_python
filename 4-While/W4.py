#Pedir un número del 1 al 10 inclusive y validarlo

number = input('Ingrese un número del 1 al 10: ')

while not number.isnumeric() or int(number) < 1 or int(number) > 10:
    number = input('Ingrese un número del 1 al 10: ')
else:
    number = int(number)
    print(f'El número {number} fue validado')