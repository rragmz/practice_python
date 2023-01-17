# Mostrar los numeros pares desde el 1 al número ingresado, y mostrar la cantidad de numeros pares encontrados
lim = int(input('Choice a number: '))
quantityEven = 0

for x in range(1, lim + 1):
    if x % 2 == 0:
        print(x)
        quantityEven = quantityEven + 1
else:
    print(f'Quantity of even numbers: {quantityEven}')