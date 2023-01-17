"""1. Para el departamento de facturación:
A. Ingresar tres precios de productos y mostrar la suma de los mismos.
B. Ingresar tres precios de productos y mostrar el promedio de los mismos.
C. ingresar tres precios de productos sumarlos y mostrar precio final (más IVA 21%)."""

sumPrices = 0
iva = 21

for x in range(3):
    price = float(input('Ingrese el precio de un artículo: '))
    sumPrices = sumPrices + price
else:
    average = format(sumPrices / 3, '.2f')
    finalPrice = format(sumPrices  + sumPrices * iva / 100, '.2f')
    print(f'Suma de los precios sin IVA: {sumPrices}\nPromedio de los precios sin IVA: {average}\nPrecio final (más IVA): {finalPrice}')