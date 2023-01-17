#Pedir 5 números e informar la suma acumulada y el promedio.
total = 0
i = 0

while i < 5:
    total += int(input('Ingrese un número: '))
    i = i+1
    promedio = format(total / 5,'.2f')

print(total, promedio)
