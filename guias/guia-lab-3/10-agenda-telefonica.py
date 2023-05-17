# 10. Crear una agenda telefonica que contenga un solo contacto. Esta agenda se debe
# guardar en un diccionario. Este diccionario debe contar con las siguientes claves:
# - Nombre, Direccion, Ciudad, Numero telefonico.
# A continuacion, agrega una nueva clave llamada “Redes Sociales” que contenga al
# menos tres nombres de perfil de diferentes redes sociales (por ejemplo, Facebook,
# Instagram y Twitter). Por ultimo, se solicita imprimir solamente el Facebook del
# contacto y luego la agenda completa actualizada.

# Titulo.
print('\n##### Modificar una lista #####\n')

# ======== Diccionarios ======== #
# Agenda principal.
agenda = {
    'Nombre'    : 'Matias Guzman',
    'Direccion' : 'Cuba #1298',
    'Ciudad'    : 'Osorno',
    'Num tel.'  : '+569 9324 4232'
}

# Clave Redes sociales.
RRSS = {
    'Facebook'   : '/mati.guz_1',
    'Instragram' : '@mati.guz_2',
    'Twitter'    : '/mati.guz_3'
}

# ======== Imprime el facebook ======== #
print('Facebook:', RRSS['Facebook'], '\n')


# Asigna el dict "RRSS" a "agenda"
agenda['RRSS'] = RRSS

# ======== Imprime la agenda ======== #
for i, k in agenda.items():
    if i != 'RRSS':
        print(i, ': ', k, sep='')

print('\nRedes sociales:')
for i, k in RRSS.items():
    print(i, ': ', k, sep='')

print()