"""
Debemos realizar la carga de 5(cinco) productos de prevención de contagio,
de cada una debo obtener los siguientes datos:
el tipo (validar "barbijo" , "jabón" o "alcohol") ,
el precio (validar entre 100 y 300),
la cantidad de unidades (no puede ser 0 o negativo y no debe superar las 1000 unidades),
la Marca y el fabricante.
Se debe Informar al usuario lo siguiente:
a) Del más barato de los alcohol, la cantidad de unidades y el fabricante
b) Del tipo con mas unidades, el promedio por compra
c) Cuántas unidades de jabones hay en total
"""
TYPES_PRODUCTS = ['barbijo', 'jabon', 'alcohol']
ALLOWED_PRICES = range(100,301)
ALLOWED_QUANTITY = range(1,1001)
def get_type():
    type_product = input('Ingrese el tipo de producto (BARBIJO/JABON/ALCOHOL): ').lower()
    while type_product.isnumeric() or type_product not in TYPES_PRODUCTS:
        type_product = input('Ingrese el tipo de producto (BARBIJO/JABON/ALCOHOL): ').lower()
    return type_product

def get_price():
    price_product = input('Ingrese el precio del producto: ')
    while not price_product.isnumeric() or float(price_product) not in ALLOWED_PRICES:
        price_product = input('Ingrese el precio del producto: ')
    return float(price_product)

def get_quantity():
    quantity_product = input('Ingrese la cantidad: ')
    while not quantity_product.isnumeric() or int(quantity_product) not in ALLOWED_QUANTITY:
        quantity_product = input('Ingrese la cantidad: ')
    return int(quantity_product)

def get_brand():
    brand_product = input('Ingrese la marca: ')
    while brand_product.isnumeric():
        brand_product = input('Ingrese la marca: ')
    return brand_product

def get_manufacturer():
    manufacturer = input('Ingrese el fabricante: ')
    while manufacturer.isnumeric():
        manufacturer = input('Ingrese el fabricante: ')
    return manufacturer

def get_average(quantity, sales):
    if sales == 0:
        return 0
    else:
        return int(quantity/sales)

def system():
    i=0
    products = []
    
    for i in range(1):
        type_product = get_type()
        price = get_price()
        quantity = get_quantity()
        brand = get_brand()
        manufacturer = get_manufacturer()
        product = {'tipo': type_product, 'precio': price, 'cantidad': quantity, 'marca': brand, 'fabricante': manufacturer}
        products.append(product)

    #Alcohol
    alcohol_products = list(filter(lambda x: x['tipo'] == "alcohol", products))

    cheapest_alcohol = min(alcohol_products, key=lambda x: x['precio'])

    #Más unidades
    type_units = {}
    for product in products:
        if product['tipo'] in type_units:
            type_units[product['tipo']]['cantidad'] += product['cantidad']
            type_units[product['tipo']]['cont'] += 1
        else:
            type_units[product['tipo']] = {'cantidad': product['cantidad'], 'cont': 1}
            
    max_type = max(type_units.items(), key=lambda x: x[1]['cantidad'])

    average_per_purchase = max_type[1]['cantidad']/ max_type[1]['cont']

    #Jabón
    soap_products = list(filter(lambda x: x['tipo'] == "jabón", products))

    soap_units = sum(product['cantidad'] for product in soap_products)


    print(f"El alcohol más barato cuesta ${cheapest_alcohol['precio']}, se llevaron {cheapest_alcohol['cantidad']} y su fabricante es: {cheapest_alcohol['fabricante']}")

    print(f"El tipo con más unidades fue {max_type[0]}, el promedio por compra es {average_per_purchase}")

    print(f"Hay un total de {soap_units} unidades de jabones")


system()

"""
alcohol_products = list(filter(lambda x: x['type'] == "alcohol", valid_products))

cheapest_alcohol = min(alcohol_products, key=lambda x: x['price'])

print("Del más barato de los alcohol:")
print("Cantidad de unidades:", cheapest_alcohol['units'])
print("Fabricante:", cheapest_alcohol['manufacturer'])

type_units = {}
for product in valid_products:
    if product['type'] in type_units:
        type_units[product['type']]['units'] += product['units']
        type_units[product['type']]['count'] += 1
    else:
        type_units[product['type']] = {'units': product['units'], 'count': 1}
        
max_type = max(type_units.items(), key=lambda x: x[1]['units'])

average_per_purchase = max_type[1]['units']/ max_type[1]['count']

print(f"Del tipo con más unidades, el promedio por compra es {average_per_purchase}")

jabon_products = list(filter(lambda x: x['type'] == "jabón", valid_products))

jabon_units = sum(product['units'] for product in jabon_products)

print(f"Hay un total de {jabon_units} unidades de jabones")"""