"""Al ingresar una hora, informar:
si está entre las 7 y las 11 : "Es de mañana."."""

hour = input('Ingrese una hora. Ex: 10: ')

while not hour.isnumeric() or int(hour) < 0 or int(hour) > 24:
    hour = input('Ingrese una hora: ')

else:
    hour = int(hour)
    if hour >= 7 and hour <= 11:
        print('Es de manaña')
