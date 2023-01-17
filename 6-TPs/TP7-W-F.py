"""Rising BTL. Empresa dedicada a la toma de datos para realizar estadísticas y censos nos pide realizar una carga de datos validada e ingresada por ventanas emergentes solamente (para evitar hacking y cargas maliciosas) y luego asignarla a cuadros de textos. 12. Los datos requeridos son los siguientes:
A. Edad, entre 18 y 90 años inclusive.
B. Sexo, “M” para masculino y “F” para femenino
C. Estado civil, 1-para soltero, 2-para casados, 3-para divorciados y 4-para viudos
D. Sueldo bruto, no menor a 8000.
E. Número de legajo, numérico de 4 cifras, sin ceros a la izquierda.
F. Nacionalidad, “A” para argentinos, “E” para extranjeros, “N” para nacionalizados."""

def valid_age():
    age = input('Ingrese su edad: ')

    while not age.isnumeric() or not int(age) in range(18,90):
        age = input('Ingrese su edad: ')
    else:
        age = int(age)
        return age

def valid_sex():
    sex = input('Ingrese su sexo (F: femenino/M: Masculino)').lower()
    
    while sex.isnumeric() or (sex != 'f' and sex != 'm'):
        sex = input('Ingrese su sexo (F: femenino/M: Masculino)').lower()
    else:
        return sex.upper()

def marital_status():
    status = input('Ingrese el número que corresponda a su estado civil\n1.Soltero\n2.Casado\n3.Divorciado\n4.Viudo')

    while not status.isnumeric() or not int(status) in range(1,4):
        status = input('Ingrese el número que corresponda a su estado civil\n1.Soltero\n2.Casado\n3.Divorciado\n4.Viudo')
    else:
        status = int(status)
        return status

def salary():
    salary = input('Ingrese su salario bruto: ')

    while not salary.isnumeric() or float(salary) < 8000:
        salary = input('Ingrese su salario en burto: ')
    else:
        salary = float(salary)
        return salary

def file_number():
    file_number = input('Ingrese su legajo: ')

    while not file_number.isnumeric() or not int(file_number) in range(1000,9999):
        file_number = input('Ingrese su legajo: ')
    else:
        file_number = int(file_number)
        return file_number

def nationality():
    nationality = input('Ingrese su Nacionalidad (A: Argentino/E: Extranjero/N: Naturalizado)').lower()
    
    while nationality.isnumeric() or (nationality != 'a' and nationality != 'e' and nationality != 'n'):
        nationality = input('Ingrese su nacionalidad (A: Argentino/E: Extranjero/N: Naturalizado)').lower()
    else:
        return nationality.upper()

def system():
    age = valid_age()
    sex = valid_sex()
    m_status = marital_status()
    b_salary = salary()
    number = file_number()
    nation = nationality()

    print(age,sex,m_status,b_salary,number,nation)

system()
