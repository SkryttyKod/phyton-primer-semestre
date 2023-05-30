# 1. Obtener la cantidad de veces que se repite la palabra “universidad” dentro del siguiente parrafo:

# “La Universidad de los Lagos es una institucion estatal fundada en 1993. Esta universidad regional
# entrega una contribucion significativa al desarrollo sostenible del territorio. Como Universidad sus
# pilares fundamentales se basan en la inclusion, pluralismo, conciencia ambiental y participacion
# democratica.”

# Guardar las palabras encontradas dentro de una tupla.

#=#=#=#=#=#=#=#=#=    INICIO    =#=#=#=#=#=#=#=#=#

# Parrafo.
parrafo = '''La Universidad de los Lagos es una institucion estatal fundada en 1993. Esta universidad regional
entrega una contribucion significativa al desarrollo sostenible del territorio. Como Universidad sus
pilares fundamentales se basan en la inclusion, pluralismo, conciencia ambiental y participacion
democratica.'''

# Inicia un lista que contendra las ocurrencias de "universidad".
occurrence_list = []

# Guarda cada palabra del parrafo como elemento de una lista.
paragraph_word_list = parrafo.split()

# Agrega las ocurrencias de "universidad" a la lista.
for i in paragraph_word_list:
    if (i == 'Universidad') or (i == 'universidad'):
        occurrence_list.append(i)

# Transforma la lista de ocurrencias en una tupla.
occurrence_tuple = tuple(occurrence_list)

# Muestra en pantalla.
print('\n##### EJERCICIO 01 #####')
print('\n- Ocurrencias de "universidad":', len(occurrence_tuple), 'veces')
print('- Palabras guardadas:', occurrence_tuple)

print('\n##### FIN EJERCICIO #####\n')

#=#=#=#=#=#=#=#=#=#=    FIN    #=#=#=#=#=#=#=#=#=#=#