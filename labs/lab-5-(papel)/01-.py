# 1. Escribir un algoritmo que permita realizar diferentes operaciones relacionadas con el sueldo
# de trabajadores, como cálculo de promedio, búsqueda del sueldo más alto de cada trabajador, y obtención del impuesto retenido.

# Se tiene la siguiente información de tres trabajadores:
# trabajadores = [ ["Juan", [700000, 650000, 690000] ], ["María", [681000, 710000, 590000] ],["Pedro", [590000, 635000, 705000] ] ]

# Pasos a seguir:
# A) Implementar una función que calcule el promedio del sueldo de cada trabajador. La función debe recibir como parámetro la 
# lista de sueldo del trabajador y devolver el promedio. El promedio tiene que tener 2 decimales como salida.

# B) Implementar una función que encuentre el sueldo más alto del trabajador. La función debe recibir como parámetro la lista de 
# sueldo del trabajador y devolver el sueldo más alto.

# C) Implementar una función que obtenga el 12.25% de retención de impuestos, porque los tres trabajadores son a honorarios.

# D) Utilizar bucles y condicionales para iterar sobre la lista de trabajadores y realizar las siguientes operaciones: 
#   - Calcular y mostrar el promedio de sueldos de cada trabajador.
#   - Encontrar y mostrar el sueldo más alto de cada trabajador.


trabajadores = [ ["Juan", [700000, 650000, 690000] ], ["María", [681000, 710000, 590000] ],["Pedro", [590000, 635000, 705000] ] ]

def promedio_por_trabajador(lista_trabajador):
    promedio = round(sum(lista_trabajador[1]) / len(lista_trabajador[1]), 2)
    return promedio

def encontrar_sueldo_max(lista_trabajador):
    sueldo_max = max(lista_trabajador[1])
    return sueldo_max

def aplicar_retencion(lista_trabajador):
    imp_retencion = []
    for i in lista_trabajador[1]:
        retencion = round((i * 0.1225), 2)
        imp_retencion.append(retencion)
    return imp_retencion


# TRABAJADOR 1: JUAN
promedio_tra_1 = promedio_por_trabajador(trabajadores[0])
sueldo_max_tra_1 = encontrar_sueldo_max(trabajadores[0])
ret_sueldo_tra_1 = aplicar_retencion(trabajadores[0])

# TRABAJADOR 2: JUAN
promedio_tra_2 = promedio_por_trabajador(trabajadores[1])
sueldo_max_tra_2 = encontrar_sueldo_max(trabajadores[1])
ret_sueldo_tra_2 = aplicar_retencion(trabajadores[1])

# TRABAJADOR 3: JUAN
promedio_tra_3 = promedio_por_trabajador(trabajadores[2])
sueldo_max_tra_3 = encontrar_sueldo_max(trabajadores[2])
ret_sueldo_tra_3 = aplicar_retencion(trabajadores[2])

print('\n##### EJERCICIO - 01 #####\n')
print('Trabajador 1: JUAN\n')

print('Promedio sueldos:', promedio_tra_1)
print('Sueldo mayor:', sueldo_max_tra_1)
print(f'Retencion: {ret_sueldo_tra_1[0]} (Sueldo 1), {ret_sueldo_tra_1[1]} (Sueldo 2), {ret_sueldo_tra_1[2]} (Sueldo 3),')

print('\nTrabajador 2: MARIA\n')

print('Promedio sueldos:', promedio_tra_2)
print('Sueldo mayor:', sueldo_max_tra_2)
print(f'Retencion: {ret_sueldo_tra_2[0]} (Sueldo 1), {ret_sueldo_tra_2[1]} (Sueldo 2), {ret_sueldo_tra_2[2]} (Sueldo 3),')

print('\nTrabajador 3: PEDRO\n')

print('Promedio sueldos:', promedio_tra_3)
print('Sueldo mayor:', sueldo_max_tra_3)
print(f'Retencion: {ret_sueldo_tra_3[0]} (Sueldo 1), {ret_sueldo_tra_3[1]} (Sueldo 2), {ret_sueldo_tra_3[2]} (Sueldo 3),')

print('\n##### EJERCICIO 01 - FIN #####\n')