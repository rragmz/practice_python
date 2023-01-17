"""pedir números hasta que el usuario quiera, sumar los que son positivos y multiplicar los negativos."""
sum_pos = 0
mult_neg = 1
answer = 'y'
i = 1

while answer == 'y':
    num = int(input('Ingrese un número: '))
    if num >= 0:
        sum_pos = sum_pos + num
    else:
        mult_neg = mult_neg * num
    answer = input('Desea seguir ingresando números? y/n: ').lower()
    i = i+1

if mult_neg != 1:
    print(sum_pos, mult_neg)
else:
    print(sum_pos)