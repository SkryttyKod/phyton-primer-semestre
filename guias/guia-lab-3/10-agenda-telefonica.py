# 10. Crear una agenda telefonica que contenga un solo contacto. Esta agenda se debe
# guardar en un diccionario. Este diccionario debe contar con las siguientes claves:
# - Nombre, Direccion, Ciudad, Numero telefonico.
# A continuacion, agrega una nueva clave llamada “Redes Sociales” que contenga al
# menos tres nombres de perfil de diferentes redes sociales (por ejemplo, Facebook,
# Instagram y Twitter). Por ultimo, se solicita imprimir solamente el Facebook del
# contacto y luego la agenda completa actualizada.

# ======== Diccionarios ======== #
# Iniciando la Agenda Telefonica (Diccionario)
tel_book = {
    'Mati G':{
        'Nombre':'Matias Guzman',
        'Direccion':'Cuba #1298',
        'Ciudad':'Osorno',
        'Num. tel.':'+56 9 3333 3333',
    }
}

# Establece el contenido de la clave "RRSS"
rrss_dicc = {'Facebook':'fb.com/Matias.Guzman',
            'Instagram':'@MatiasG',
            'Twitter': '@matiG'}

# ======== Mostrar en pantalla ======== #
print('\n##### Agenda Telefonica #####\n')

# Imprime la agenda original
print('= Agenda original =')
print('Mati G:')
for key, value in tel_book['Mati G'].items():
    print(f'{key}: {value}')
print('')

# Añade una clave "RRSS" a la clave "Mati G." que tendra el valor de "rrss_dicc"
tel_book['Mati G']['RRSS'] = rrss_dicc

# Extrae el Facebook del contacto.
fb_contact = tel_book['Mati G']['RRSS']['Facebook']

# Muestra el facebook
print('= Facebook =')
print(fb_contact)
print()

# Imprime la agenda modificada
print('= Agenda modificada =')
print('Mati G:')
for key, value in tel_book['Mati G'].items():
    print(f'{key}: {value}')
print()
