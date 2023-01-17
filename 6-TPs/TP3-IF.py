"""Las lámparas están al mismo precio de $35 pesos final.
A. Si compra 6 o más lamparitas bajo consumo tiene un descuento del 50%.
B. Si compra 5 lamparitas bajo consumo marca "ArgentinaLuz" se hace un descuento del 40 % y si es de otra marca el descuento es del 30%.
C. Si compra 4 lamparitas bajo consumo marca "ArgentinaLuz" o “FelipeLamparas” se hace un descuento del 25 % y si es de otra marca el descuento es del 20%.
D. Si compra 3 lamparitas bajo consumo marca "ArgentinaLuz" el descuento es del 15%, si es “FelipeLamparas” se hace un descuento del 10 % y si es de otra marca un 5%.
E. Si el importe final con descuento suma más de $120 se debe sumar un 10% de ingresos brutos en informar del impuesto con el siguiente mensaje: ”IIBB Usted pago X”, siendo X el impuesto que se pagó."""

def is_positive(arg):
    result = 1
    if not arg.isnumeric() or int(arg) < 0:
        result = 0
    return result 

def get_quantity():
    input('Ingrese la cantidad de lámparas que desea comprar: ')
    while not is_positive(quantity) or int(quantity) < 0:
        quantity = input('Ingrese la cantidad de lámparas que desea comprar: ')
    return int(quantity)

def get_brand():
    input('Ingrese el número correspondiente a la marca que desea comprar:\n1.ArgentinaLuz\n2.FelipeLamparas\n3.Otra\nSu selección: ')
    while not is_positive(brand) or int(brand) not in [1,2,3]:
        brand = input('Ingrese el número correspondiente a la marca que desea comprar:\n1.ArgentinaLuz\n2.FelipeLamparas\n3.Otra\nSu selección: ')
    return int(brand)

def def_average(quantity, brand):
    if quantity == 3:
        if brand == 1:
            average = 0.15
        elif brand == 2:
            average = 0.10
        else:
            average = 0.05

    elif quantity == 4:
        if brand in [1,2]:
            average = 0.25
        else:
            average = 0.20

    elif quantity == 5:
        if brand == 1:
            average = 0.40
        else:
            average = 0.30

    elif quantity >= 6:
        average = 0.50
    else:
        average = 0
    return average


def total_import(price, quantity, average):
    total = price * quantity
    return float(format(total - price * quantity * average, '.2f'))


def final_price(quantity, brand):
    lamp = 35
    final_amount = total_import(lamp, quantity, def_average(quantity,brand))

    if final_amount > 120:
        final_amount = total_import(lamp, quantity, 0.5) + final_amount * 0.1
        iibb = format(final_amount * 0.1,'.2f')
        print(f'El importe total a pagar es: {final_amount}, de IIBB pagó {iibb}')
    else:
        print(f'El importe total a pagar llevando {quantity} lamparas de la marca {brand} es ${final_amount}')

quantity = get_quantity()
brand = get_brand()
final_price(quantity, brand)

