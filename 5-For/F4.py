# Repetir el pedido de número hasta que ingresemos el 9

for x in range(100):
    number = int(input('Choice a number: '))
    if number == 9:
        break
    else:
        print(number)