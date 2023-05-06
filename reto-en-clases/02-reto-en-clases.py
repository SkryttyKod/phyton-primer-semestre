print('#### Laboratorio num 2 ####')

# Inicia un diccionario vacio
dicc = {}

# Toma los valores de ingreso para las variables.
nombre_estudiante = input('Ingrese nombre del usuario: ')
nombre_asignatura = input('Ingrese nombre de asignatura: ')
nota_lab_1 = float(input('Ingrese nota del laboratorio 1: '))
nota_lab_2 = float(input('Ingrese nota laboratorio 2: '))

# Calcular la nota final
nota_final = (nota_lab_1 * 0.3) + (nota_lab_2 * 0.7)

dicc['Nombre de estudiante'] = nombre_estudiante
dicc['Nombre de asignatura'] = nombre_asignatura
dicc['Nota lab 1'] = nota_lab_1
dicc['Nota lab 2'] = nota_lab_2

# Imprime informacion ingresada
print("\nInformación ingresada:")

# Imprime el diccionario.
# Recorre clave y valor
for clave, valor in dicc.items(): # sobre items del diccionario
    print(clave + ": " + str(valor)) # print valor final
print("\nLa nota final del estudiante es: {:.1f}".format(nota_final)) # print nota final

