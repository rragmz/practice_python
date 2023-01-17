"""pedir números hasta que el usuario quiera, mostrar:
1-Suma de los negativos. 2-Suma de los positivos. 3-Cantidad de positivos. 4-Cantidad de negativos. 5-Cantidad de ceros. 6-Cantidad de números pares. 7-Promedio de positivos. 8-Promedios de negativos. 9-Diferencia entre positivos y negativos, (positvos-negativos)."""

sum_pos = 0
sum_neg = 0
quantity_neg = 0
quantity_pos = 0
quantity_zero = 0
quantity_even = 0
answer = 'y'
i = 0

while answer == 'y':
    number = int(input('Ingrese un número: '))
    if (number % 2) == 0:
        quantity_even = quantity_even + 1

    if number > 0:
        quantity_pos = quantity_pos + 1
        sum_pos = sum_pos + number

    elif number == 0:
        quantity_zero = quantity_zero + 1
    
    elif number < 0:
        quantity_neg = quantity_neg + 1
        sum_neg = sum_neg + number

    answer = input('Desea seguir ingresando números?: ')
    i = i + 1
else:
    average_pos = format(sum_pos/quantity_pos, '.2f')
    average_neg = format(sum_neg/quantity_neg, '.2f')
    dif = sum_pos - sum_neg
    print(f'1. Suma de los negativos: {sum_neg}\n2. Suma de los positivos: {sum_pos}\n3. Cantidad de positivos: {quantity_pos}\n4. Cantidad de negativos: {quantity_neg}\n5. Cantidad de ceros: {quantity_zero}\n6. Cantidad de pares: {quantity_even}\n7. Promedio de positivos: {average_pos}\n8. Promedio de negativos: {average_neg}\n9. Diferencia entre positivos y negativos: {dif}')

