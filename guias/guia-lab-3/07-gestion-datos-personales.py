# 7. Crear una lista con nombres de 5 trabajadores y otra lista con las edades de
# estos 5 trabajadores, Se solicita relacionar ambas listas en una sola estructura.
# La salida puede ser en tuplas o en un diccionario.

# ======== Listas y Variables ======== #
workers_name = ['Jaime Garcia', 'Laura Martinez', 'Carlos Gonzales', 'Andrea Gomez', 'Manuel Herrera']
workers_age = ['28', '42', '37', '51', '24']
workers_dicc = {}
aux = 0

# ======== Llenando el diccionario ======== #
for i in workers_name:
    workers_dicc[i] = workers_age[aux]
    aux += 1

# ======== Mostrar en pantalla ======== #
print('\n##### Gestion de datos personales #####\n')
print('Lista nombres:\n', workers_name, '\n', sep='')
print('Lista edades:\n', workers_age, '\n', sep='')
print('Datos ordenados:')
print(workers_dicc)
print()