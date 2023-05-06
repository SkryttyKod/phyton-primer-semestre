### 01 - RETO EN CLASES ###

# Escribe un programa que le pida al usuario el nombre del estudiante, el nombre de la asignatura, 
# la nota del laboratorio 1 y la nota del laboratorio 2. El programa debe calcular la nota final como el 30% 
# de la nota del laboratorio 1 más el 70% de la nota del laboratorio 2. Luego, el programa debe almacenar la información 
# ingresada por el usuario en un diccionario y mostrarla en la pantalla.
# La información debe mostrarse en el siguiente formato:

# Nombre de estudiante: [nombre_estudiante]
# Nombre de asignatura: [nombre_asignatura]
# Nota lab 1: [nota_lab_1]
# Nota lab 2: [nota_lab_2]
# La nota final del estudiante es: [nota_final]"

### 𝕀𝕟𝕚𝕔𝕚𝕠 𝕕𝕖𝕝 𝕣𝕖𝕥𝕠 ###

# Inicia un diccionario vacio
dicc = {}

# Toma los valores de ingreso para las variables.
nombre_estudiante = input('Ingrese nombre del usuario: ')
nombre_asignatura = input('Ingrese nombre de asignatura: ')
nota_lab_1 = float(input('Ingrese nota del laboratorio 1: '))
nota_lab_2 = float(input('Ingrese nota laboratorio 2: '))

# Calcular la nota final
nota_final = (nota_lab_1 * 0.3) + (nota_lab_2 * 0.7)

# Agrega las claves al diccionario, seguido de los valores (datos ingresados).
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

### 𝔽𝕚𝕟 𝕕𝕖𝕝 𝕣𝕖𝕥𝕠 ###