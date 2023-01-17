"""Al presionar el Botón, asignar una nota RANDOM al examen y mostrar:
"EXCELENTE" para notas igual a 9 o 10,
"APROBÓ" para notas mayores a 4,
"Vamos, la proxima se puede" para notas menores a 4"""

import random

number = random.randint(1,10)

if number >= 9:
    print('EXCELENTE, su nota es:', number)
elif number > 4:
    print('APROBÓ, su nota es:', number)
else:
    print('Vamos, la proxima se puede, su nota es: ', number)