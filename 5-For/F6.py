# Mostrar los numeros divisores desde el 1 al número ingresado, y mostrar la cantidad de numeros divisores encontrados

lim = int(input('Choice a number: '))
quantityDiv = 0

for x in range(1, lim + 1):
    if lim % x == 0:
        print(x)
        quantityDiv = quantityDiv + 1
else:
    print(f'Quantity of divider numbers: {quantityDiv}')