### 03 - RETO EN CLASES ###

# Elaborar un algoritmo que sea capaz de solicitar por teclado los nombres de tres pacientes,
# sus pesos, su altura y su edad correspondientes. La edad del paciente solo debe permitir enteros
# y debe ser valida. Toda la informacion debe guardarse en tuplas.

### 𝕀𝕟𝕚𝕔𝕚𝕠 𝕕𝕖𝕝 𝕣𝕖𝕥𝕠 ###

# Iniciando tuplas de datos
patient_name = ()
patient_age = ()
patient_weight = ()
patient_height = ()

# iniciando tuplas por paciente
patient_1 = ()
patient_2 = ()
patient_3 = ()

#### PRIMER PACIENTE ####

print('\n#### INGRESO DATOS PRIMER PACIENTE ####\n')

#NOMBRE
pat_name = input('Ingrese el nombre del primer paciente: ')
patient_name += (pat_name,)

# EDAD
while True:
    pat_age = int(input('Ingrese la edad del primer paciente: '))
    if (pat_age < 0) or (pat_age > 140):
        continue
    else:
        patient_age += (pat_age,)
        break

# PESO
while True:
    pat_wei = float(input('Ingrese el peso del primer paciente (Kg.): '))
    if (pat_wei < 0) or (pat_wei > 700):
        continue
    else:
        patient_weight += (pat_wei,)
        break

# ESTATURA
while True:
    pat_hei = int(input('Ingrese la estatura del primer paciente (Cm): '))
    if (pat_hei < 20) or (pat_hei > 300):
        continue
    else:
        patient_height += (pat_hei,)
        break

#### SEGUNDO PACIENTE###

print('\n#### INGRESO DATOS SEGUNDO PACIENTE ####\n')

#NOMBRE
pat_name = input('Ingrese el nombre del segundo paciente: ')
patient_name += (pat_name,)

# EDAD
while True:
    pat_age = int(input('Ingrese la edad del segundo paciente: '))
    if (pat_age < 0) or (pat_age > 140):
        continue
    else:
        patient_age += (pat_age,)
        break

# PESO
while True:
    pat_wei = float(input('Ingrese el peso del tercer paciente (Kg.): '))
    if (pat_wei < 0) or (pat_wei > 700):
        continue
    else:
        patient_weight += (pat_wei,)
        break

# ESTATURA
while True:
    pat_hei = int(input('Ingrese la estatura del tercer paciente (Cm): '))
    if (pat_hei < 20) or (pat_hei > 300):
        continue
    else:
        patient_height += (pat_hei,)
        break

#### TERCER PACIENTE###

print('\n#### INGRESO DATOS TERCER PACIENTE ####\n')

#NOMBRE
pat_name = input('Ingrese el nombre del tercer paciente: ')
patient_name += (pat_name,)

# EDAD
while True:
    pat_age = int(input('Ingrese la edad del tercer paciente: '))
    if (pat_age < 0) or (pat_age > 140):
        continue
    else:
        patient_age += (pat_age,)
        break

# PESO
while True:
    pat_wei = float(input('Ingrese el peso del tercer paciente (Kg.): '))
    if (pat_wei < 0) or (pat_wei > 700):
        continue
    else:
        patient_weight += (pat_wei,)
        break

# ESTATURA
while True:
    pat_hei = int(input('Ingrese la estatura del tercer paciente (Cm): '))
    if (pat_hei < 20) or (pat_hei > 300):
        continue
    else:
        patient_height += (pat_hei,)
        break

# Dividiendo los datos a una tupla por paciente.
patient_1 += (patient_name[0],patient_age[0],patient_weight[0],patient_height[0])
patient_2 += (patient_name[1],patient_age[1],patient_weight[1],patient_height[1])
patient_3 += (patient_name[2],patient_age[2],patient_weight[2],patient_height[2])

print(patient_1)
print(patient_2)
print(patient_3)

### 𝔽𝕚𝕟 𝕕𝕖𝕝 𝕣𝕖𝕥𝕠 ###