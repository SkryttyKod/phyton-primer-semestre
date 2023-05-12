
# 5. Crear un algoritmo que solicite por consola las 3 notas de los laboratorios realizados en el ramo de 
# Programacion. Luego obtener el promedio ponderado de la siguiente manera:
# - Promedio ponderado: Lab 1 * 0,3 + Lab 2 * 0,4 + Lab 3 * 0,3
# Si el promedio es menor a 4,0 debe imprimir el mensaje que el estudiante reprobo la asignatura. Si el 
# promedio es superior a 4,0, indicar que el estudiante aprobo la asignatura. Si la nota es superior 6,0, 
# debe mostrar el mensaje: el estudiante aprobo con distincion.

# Titulo.
print('\n##### Calcular nota #####\n     -Programacion -\n')

# ======== Ingreso de notas ======== #
# Ingreso nota Lab 1.
while True:
    try:
        lab_1 = float(input('Ingrese la nota del Lab 1: '))
        if (lab_1 >= 1.0) and (lab_1 <= 7.0):
            break
        else:
            print('Ingrese una nota valida (1.0-7.0).')
    except ValueError:
        print('Ingrese una nota valida (1.0-7.0).')

# Ingreso nota Lab 2.
while True:
    try:
        lab_2 = float(input('Ingrese la nota del Lab 2: '))
        if (lab_2 >= 1.0) and (lab_2 <= 7.0):
            break
        else:
            print('Ingrese una nota valida (1.0-7.0).')
    except ValueError:
        print('Ingrese una nota valida (1.0-7.0).')

# Ingreso nota Lab 3.
while True:
    try:
        lab_3 = float(input('Ingrese la nota del Lab 3: '))
        if (lab_3 >= 1.0) and (lab_3 <= 7.0):
            break
        else:
            print('Ingrese una nota valida (1.0-7.0).')
    except ValueError:
        print('Ingrese una nota valida (1.0-7.0).')

# ======== Calcular el promedio ======== #
f_note = lab_1 * 0.3 + lab_2 * 0.4 + lab_3 * 0.3

# ======== Mostrar en pantalla ======== #
# Si el promedio es menor a 4.0.
if f_note < 4.0:
    print('\nPromedio final:', f_note, '\nEstado: [REPROBADO]\n')

# Si el promedio esta entre 4.0 y 5.9.
elif (f_note >= 4.0) and (f_note < 6.0):
    print('\nPromedio final:', f_note, '\nEstado: [APROBADO]\n')

# Si el promedio es 6.0 o superior.
else:
    print('\nPromedio final:', f_note, '\nEstado: [APROBADO CON DISTINCION]\n')