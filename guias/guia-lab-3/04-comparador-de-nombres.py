
# 4. Elaborar un algoritmo que solicite al usuario su nombre y el nombre de otra
# persona. Luego, mostrar en pantalla un mensaje que indique si ambos nombres
# comienzan con la misma letra o si terminan con la misma letra, o si difieren tanto
# en la letra inicial como en la final. Por ejemplo, si los nombres ingresados son
# Belinda y Beatriz, se mostrara un mensaje que indique que ambos nombres comienzan con la 
# misma letra. Si los nombres son Leonardo y Gonzalo, se mostrara un mensaje que indique
# que ambos nombres terminan con la misma letra.

# Titulo.
print('\n##### Comparador de nombres #####')

print('''
Los nombres ingresados deben
contener solo letras (3 o +).
''')

# ======== Ingreso de nombres ======== #
# Primer nombre.
while True:
    name_1 = input('Ingresa el 1° nombre: ')
    long = len(name_1)
    if name_1.isalpha() and (long >= 3):
        break
    else:
        print('Ingresa un nombre valido (min. 3)')
        continue

# Segundo nombre.
while True:
    name_2 = input('Ingresa el 2° nombre: ')
    long = len(name_2)
    if name_2.isalpha() and (long >= 3):
        break
    else:
        print('Ingresa un nombre valido (min. 3)')
        continue

# ======== Transformaciones ======== #
# A minusculas.
name_1_min = name_1.lower()
name_2_min = name_2.lower()

# Dividiendo los nombres en listas.
name_1_list = list(name_1_min)
name_2_list = list(name_2_min)

print('\n- Palabra 1:', name_1)
print('- Palabra 2:', name_2)

# ======== Comparaciones ======== #
# Si los  nombres ingresados son iguales.
if name_1_min == name_2_min:
    print('\nLas palabras son iguales.\n')

# Si los nombres coinciden en la primera y ultima letra.
elif (name_1_min[0] == name_2_min[0]) and (name_1_min[-1] == name_2_min[-1]):
    print('\nLas palabras comienzan y\nterminan con las mismas letras.\n')

# Si los nombres coinciden en la primera letra.
elif (name_1_min[0] == name_2_min[0]):
    print('\nLas palabras coinciden al principio\n')

# Si los nombres coinciden en la ultima letra.
elif (name_1_min[-1] == name_2_min[-1]):
    print('\nLas palabras coinciden al final\n')

# Si no hay coincidencias.
else:
    print('\nNo hay coincidencias.\n')