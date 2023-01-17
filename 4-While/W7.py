#Pedir números hasta que el usuario quiera y mostrar la suma total y el promedio
total = 0
answer = 'y'
i = 1

while answer == 'y':
    total = total + int(input('Ingrese un número: '))
    answer = input('Desea seguir ingresando números? y/n: ').lower()
    promedio = format(total/i,'.2f')
    i = i+1

print(total, promedio)