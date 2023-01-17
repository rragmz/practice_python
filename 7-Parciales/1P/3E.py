"""Bienvenidos.
En el ingreso a un viaje en avion nos solicitan nombre , edad, sexo("f" o "m") y estado civil("soltero", "casado" o "viudo")y temperatura corporal.
a) El nombre de la persona con mas temperatura.
b) Cuantos mayores de edad estan viudos
c) La cantidad de hombres que hay solteros o viudos.
d) cuantas personas de la tercera edad( mas de 60 años) , tienen mas de 38 de temperatura
e) El promedio de edad entre los hombres solteros"""

MAR_STATUS = ['soltero', 'casado', 'viudo']
PASSENGERS = 3
def get_name():
    name = input('Ingrese su nombre: ')
    while name.isnumeric():
        name = input('Ingrese su nombre: ')
    else: return name

def get_age():
    age = input('Ingrese su edad: ')
    while not age.isnumeric() or int(age) not in range(1,106):
        age = input('Ingrese su edad: ')
    else: return int(age)

def get_sex():
    sex = input('Ingrese su sexo(f: femenino/m:masculino): ').lower()
    while sex.isnumeric() or sex != 'f' and sex != 'm':
        sex = input('Ingrese su sexo(f: femenino/m:masculino): ').lower()
    else:
        return sex

def get_marital_status():
    marital_status = input('Ingrese su estado civil (soltero/casado/viudo): ').lower()
    while marital_status.isnumeric() or marital_status not in MAR_STATUS:
        marital_status = input('Ingrese su estado civil (soltero/casado/viudo): ').lower()
    else: return marital_status

def get_temperature():
    temperature = input('Ingrese su temperatura corporal: ')
    while not temperature.isnumeric() or float(temperature) not in range(30,45):
        temperature = input('Ingrese su temperatura corporal: ')
    else: return float(temperature)

def system():
    i = 0
    cont_legal_widower = 0
    cont_man_single = 0
    cont_man_widower = 0
    acum_age_man_single = 0
    cont_old_high_temperature = 0

    for i in range(PASSENGERS):
        name = get_name()
        age = get_age()
        sex= get_sex()
        marital_status = get_marital_status()
        temperature = get_temperature()

        if i == 0 or more_temperature < temperature:
            more_temperature = temperature
            name_more_temperature = name
        
        if age >= 18:
            if marital_status == 'viudo':
                cont_legal_widower = cont_legal_widower + 1
        elif age >= 60:
            if temperature > 38:
                cont_old_high_temperature = cont_old_high_temperature + 1

        if sex == 'm' and marital_status == 'soltero':
            cont_man_single = cont_man_single + 1
            acum_age_man_single = acum_age_man_single + age
        elif sex == 'm' and marital_status == 'viudo':
            cont_man_widower = cont_man_widower + 1

    total_man_single_widower = cont_man_single + cont_man_widower
    average_age_single_man = acum_age_man_single / cont_man_single

    print(f'{name_more_temperature} tiene la temperatura más alta: {more_temperature}')
    print(f'La cantidad de mayores de edad viudos es de: {cont_legal_widower}')
    print(f'La cantidad de hombres solteros y viudos es de: {total_man_single_widower}')
    print(f'Hay {cont_old_high_temperature} personas de más de 60 años con una temperatura mayor a 38°C')
    print(f'El promedio de edad de los hombres solteros es de {average_age_single_man} años')

system()