# 2. Escribir un programa que pida al usuario ingresar dos palabras y las guarde en
# dos variables diferentes. Luego imprimir cual palabra tiene mas caracteres y cual
# tiene menos caracteres.

# Lista que contendra las palabras ingresadas.
word_list = []

# Titulo.
print('\n##### Comparador de palabras #####\n')

# ======== Ingreso de palabras ======== #
for i in range(1, 3):
    sw = True
    while sw == True:
        try:
            word_entry = input(f'Ingrese la {i}° palabra: ')
            if word_entry.isalpha():
                word_list.append(word_entry)
                sw = False
            else:
                print('Ingrese una palabra valida.')

        except:
            print('Ingrese una palabra valida.')

# ======== De lista a variables ======== #
word_1 = word_list[0]
word_2 = word_list[1]

# ======== Comparador de palabras ======== #
# Si la 1ra palabra es mas larga.
if len(word_1) > len(word_2):
    longest_word = word_1
    shortest_word = word_2
    print('\nLa palabra mas larga es:', longest_word)
    print('La palabra mas corta es:', shortest_word)

# Si las palabras miden lo mismo.
elif len(word_1) == len(word_2):
    print('\nLas palabras tienen la misma cantidad de caracteres.')

# Si la 2da palabra es mas larga.
else:
    longest_word = word_2
    shortest_word = word_1
    print('\nLa palabra mas larga es:', longest_word)
    print('La palabra mas corta es:', shortest_word)