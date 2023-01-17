"""una agencia de viajes debe sacar las tarifas de los viajes , se cobra $15.000 por cada estadia como base, se pide el ingreso de una estacion del año y localidad para vacacionar para poder calcular el precio final

en Invierno: bariloche tiene un aumento del 20% cataratas y Cordoba tiene un descuento del 10% Mar del plata tiene un descuento del 20%

en Verano: bariloche tiene un descuento del 20% cataratas y Cordoba tiene un aumento del 10% Mar del plata tiene un aumento del 20%

en Otoño y Primavera: bariloche tiene un aumento del 10% cataratas tiene un aumento del 10% Mar del plata tiene un aumento del 10% y Cordoba tiene el precio sin descuento
"""

hosting = 15000
station = input('Ingrese la estación del año en la que va a vacacionar (Invierno/Verano/Otoño/Primavera): ')
location = input('Ingrese la localidad a la que desea viajar (Bariloche/Cataratas/Cordoba/Mar del Plata): ')

while station.isnumeric() or location.isnumeric():
    station = input('Ingrese la estación del año en la que va a vacacionar (Invierno/Verano/Otoño/Primavera): ')
    location = input('Ingrese la localidad a la que desea viajar (Bariloche/Cataratas/Cordoba/Mar del Plata): ')

else:
    station = station.lower()
    location = location.lower()

    #INVIERNO 
    if station == 'invierno':
        #Bariloche +20%
        if location == 'bariloche':
            porcentaje = 20
            hosting = hosting + hosting * porcentaje / 100

        #Cataratas o Cordoba -10%
        elif location == 'cataratas' or location == 'cordoba':
            porcentaje = 10
            hosting = hosting - hosting * porcentaje / 100
        
        #Mar del Plata -20%
        elif location == 'mar del plata':
            porcentaje = 20
            hosting = hosting - hosting * porcentaje / 100

    #VERANO
    elif station == 'verano':
        #Bariloche -20%
        if location == 'bariloche':
            porcentaje = 20
            hosting = hosting - hosting * porcentaje / 100

        #Cataratas o Cordoba +10%
        elif location == 'cataratas' or location == 'cordoba':
            porcentaje = 10
            hosting = hosting + hosting * porcentaje / 100
        
        #Mar del Plata +20%
        elif location == 'mar del plata':
            porcentaje = 20
            hosting = hosting + hosting * porcentaje / 100

    ##OTOÑO/PRIMAVERA
    elif station == 'otoño' or station == 'primavera':
        if location == 'bariloche' or location == 'cataratas' or location == 'mar del plata':
            porcentaje = 10
            hosting = hosting + hosting * porcentaje / 100
        elif location == 'cordoba':
            hosting

print(f'Vacacionar en {station} en {location} le cuesta: {hosting}')
    
    