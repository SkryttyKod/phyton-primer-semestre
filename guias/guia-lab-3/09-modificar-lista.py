# 9. Se tiene la siguiente lista de enteros:
# numeros = [4, 3, 8, 12, 6, 10, 14, 3, 6]
# Se solicita:
# a) Eliminar el ultimo elemento de la lista
# b) Agregar en la primera posicion el numero 2
# c) Eliminar los numeros duplicados de la lista
# d) Obtener la media y la mediana de la lista

# ======== Listas ======== #
nums = [4, 3, 8, 12, 6, 10, 14, 3, 6]
nums_no_repeat = []

# Formato de texto para mostrar en pantalla.
nums_txt = ', '.join(str(num) for num in nums)

# ======== Mostrar en pantalla ======== #
print('\n##### Modificar una lista #####\n')

# Lista original
print('- Lista original:', nums_txt)

# Borra el ultimo elemento.
del nums[-1]
nums_txt = ', '.join(str(num) for num in nums)
print('- Elimina el ultimo elemento:', nums_txt)

# Agrega "2" en la 1era posicion.
nums.insert(0, 2)
nums_txt = ', '.join(str(num) for num in nums)
print('- Agrega "2" en la 1era pos.:', nums_txt)

# Elimina numeros duplicados.
for i in nums:
    if i not in nums_no_repeat:
        nums_no_repeat.append(i)
nums_txt = ', '.join(str(num) for num in nums_no_repeat)
print('- Elimina los repetidos:', nums_txt)
print('')

# Ordena los numeros de la lista de menor a mayor.
nums_sorted = sorted(nums_no_repeat)

# ======== Calcular la media y la mediana ======== #
# Media
mean = (nums_sorted[0]+nums_sorted[1]+nums_sorted[2]+nums_sorted[3]+nums_sorted[4]+nums_sorted[5]+nums_sorted[6]+nums_sorted[7]) / 8

# Mediana
median = (nums_sorted[3]+nums_sorted[4]) / 2

print(' Media:', mean)
print(' Mediana:', median)
print()
