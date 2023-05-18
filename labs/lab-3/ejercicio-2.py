

# Listas
a = [21,8,15,3,12]
b = [10,9,12,15,18]
c = [2,3,8,9,12]

print('\n######### EJERCICIO 2 #########')
# A) Concatenar todas las listas e imprimir la lista obtenida.
full_list = a + b + c
print('\n-Lista concatenada:', full_list)

# B) Agregar el número 20 en la penúltima posición de la lista.
full_list.insert(-1, 20)
print('\n-Agrega el 20 en la penultima posicion:',full_list)

# C) Ordenar la lista de forma descendente.
sorted_list = sorted(full_list)
full_list_inverse = []
for i in sorted_list:
    full_list_inverse.insert(0, i)
print('\n-Lista ordenada descendentemente:',full_list_inverse)


# D) Insertar la lista [4,5,6] en la última posición de la lista ordenada
full_list_inverse.append([4, 5, 6])
print('\n-Agrega una lista en la ultima posicion:',full_list_inverse)

# E) Sumar todos los números dentro de la lista.
sum_sublist = full_list_inverse[-1][0] + full_list_inverse[-1][1] + full_list_inverse[-1][2]
sum_list = full_list_inverse[0]+full_list_inverse[1]+full_list_inverse[2]+full_list_inverse[3]+full_list_inverse[4]+full_list_inverse[5]+full_list_inverse[6]+full_list_inverse[7]+full_list_inverse[8]+full_list_inverse[9]+full_list_inverse[10]+full_list_inverse[11]+full_list_inverse[12]+full_list_inverse[13]+full_list_inverse[14]+full_list_inverse[15]
sum_full_list = sum_list + sum_sublist

print('\n-La suma de todos los elementos:',sum_full_list)

# F) Obtener el promedio simple de la lista

sublist = full_list_inverse[-1]
del full_list_inverse[-1]
full_list_inverse += sublist

prom_simp = sum(full_list_inverse) / len(full_list_inverse)

print('\n-El promedio simple es:',prom_simp)
print('')