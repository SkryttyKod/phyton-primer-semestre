# 1. Realizar un algoritmo que indique el numero menor y el numero mayor entre tres
# enteros leidos por consola. Solo se deben ingresar numeros enteros.

# ======== Variables ======== #
num_list = []
user_num = 0

# Titulo.
print()
print('##### Detector de num min. y max. #####\n')

# ======== Ingreso de numeros ======== #
for i in range(1, 4):
    sw = True
    while sw == True:
        try:
            user_list = int(input(f'Ingresa el {i}° numero (entero): '))
            num_list.append(user_list)
            sw = False
        except ValueError:
            print('Ingrese un numero valido.')

# Ordena la lista de menor a mayor.
num_list_sorted = sorted(num_list)  

# ======== Mostrar en pantalla ======== #
print('\nLista original: ', num_list[0], ', ', num_list[1], ', ', num_list[2], sep='')
print('Lista ordenada: ', num_list_sorted[0], ', ', num_list_sorted[1], ', ', num_list_sorted[2], sep='')
print('Num. menor:', num_list_sorted[0], '| Num. mayor:', num_list_sorted[2], '\n')