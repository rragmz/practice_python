"""Realizar el algoritmo que permita ingresar los datos de una compra productos de la construccion, hasta que el cliente quiera:
Tipo validad("arena";"cal";"cemento")
Cantidad de bolsas,
Precio por bolsa (más de cero ),

Si compro más de 10 bolsas en total tenes 15% de descuento sobre el total a pagar.
Si compro más de 30 bolsas en total tenes 25% de descuento sobre el total a pagar.
a) El importe total a pagar , bruto sin descuento y...
b) el importe total a pagar con descuento(solo si corresponde)
d) Informar el tipo con mas cantidad de bolsas.
f) El tipo mas caro"""

PRODUCTS = ['ARENA', 'CAL', 'CEMENTO']

def get_type():
    type_product = input('Ingrese el tipo de producto (ARENA/CAL/CEMENTO): ').upper()
    while type_product.isnumeric() or type_product not in PRODUCTS:
        type_product = input('Ingrese el tipo de producto (ARENA/CAL/CEMENTO): ').upper()
    else:
        return type_product

def get_quantity():
    quantity = input('Ingrese la cantidad de bolsas: ')
    while not quantity.isnumeric() or int(quantity) < 0:
        quantity = input('Ingrese la cantidad de bolsas: ')
    else:
        return int(quantity)

def get_price():
    price = input('Ingrese el precio: ')
    while not price.isnumeric() or float(price) < 0:
        price = input('Ingrese el precio: ')
    else:
        return float(price)

def system():
    answer = 's'
    average = 1
    acum_bag = 0

    acum_arena = 0
    acum_cal = 0
    acum_cemento = 0

    
    total_without_average = 0
    

    i=0
    while answer == 's':
        type_product = get_type()
        quantity = get_quantity()
        price = get_price()
        
        acum_bag = acum_bag + quantity

        if type_product == 'ARENA':
            acum_arena = acum_arena + quantity
        elif type_product == 'CAL':
            acum_cal = acum_cal + quantity
        else:
            acum_cemento = acum_cemento + quantity
        
        if i == 0 or price_more_expensive < price:
            price_more_expensive = price
            type_more_expensive = type_product
            i = i+1

        total_without_average = total_without_average + quantity * price
        answer = input('Quiere seguir agregando artículos? s/n: ').lower()
    
    #Porcentaje de descuento
    if acum_bag > 10:
        average = 0.15
    elif acum_bag > 30:
        average = 0.3

    total_with_average = total_without_average - total_without_average * average

    #El tipo con más cantidad de bolsas
    if acum_arena > acum_cal and acum_arena >= acum_cemento:
        more_bags = 'Arena'
        quantity_more_bags = acum_arena
    elif acum_cal > acum_arena and acum_cal > acum_cemento:
        more_bags = 'Cal'
        quantity_more_bags = acum_cal
    else:
        more_bags = 'Cemento'
        quantity_more_bags = acum_cemento



    print(f'El importe total a pagar bruto es: ${total_without_average}')
    print(f'El importe total a pagar con descuento es: ${total_with_average}')
    print(f'El tipo con más cantidad de bolsas es: {more_bags}, con una cantidad de: {quantity_more_bags}')
    print(f'EL tipo más caro es {type_more_expensive} y su precio ${price_more_expensive}')

system()