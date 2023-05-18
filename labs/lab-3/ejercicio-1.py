# A) Guardar la información de la tabla en un diccionario, luego imprimir el diccionario por consola.

dict_regions = {'Los lagos' : {'Id' : '14', 'Superficie' : '18429', 'Habitantes' : '404432'},
                'Magallanes': {'Id' : '12', 'Superficie' : '1382291', 'Habitantes' : '166533'}}

print('\n######### EJERCICIO 1 #########')

print('\n-Diccionario original:',dict_regions)

# B) Crear una nueva clave al diccionario llamada “Densidad”. La densidad poblacional se calcula 
# de la siguiente forma: (Densidad = Habitantes/Superficie). Solamente debe tener 1 decimal la salida del resultado.

dict_regions['Los lagos']['Densidad'] = round((((int(dict_regions['Los lagos']['Habitantes']) / int(dict_regions['Los lagos']['Superficie'])))), 1)
dict_regions['Magallanes']['Densidad'] = round((((int(dict_regions['Magallanes']['Habitantes']) / int(dict_regions['Magallanes']['Superficie'])))), 1)

print('\n-Añadiendo la clave "Densidad":',dict_regions)

# C) Agregar otra clave llamada “Capital”, correspondiente a la capital de cada región

dict_regions['Los lagos']['Capital'] = 'Valdivia'
dict_regions['Magallanes']['Capital'] = 'Punta arenas'

print('\n-Añadiendo la clave "Capital":',dict_regions)

# D) Agregar otra clave con el nombre “Comunas” la cual será una lista de 3 comunas de cada región como mínimo.

dict_regions['Los lagos']['Comunas'] = ['Río Bueno', 'La Unión', 'Paillaco']
dict_regions['Magallanes']['Comunas'] = ['Cabo de Hornos', 'Puerto Williams', 'Porvenir']
print('\n-Añadiendo la clave "Comunas":',dict_regions)

# E) Crear una última clave llamada “Provincia” la cual almacenará el nombres de las provincias correspondiente 
# a cada región. Las provincias se guardarán en tuplas.

dict_regions['Los lagos']['Provincias'] = ('Ranco', 'Valdivia')
dict_regions['Magallanes']['Provincia'] = ('Antártica Chilena', 'Magallanes', 'Tierra del Fuego', 'Última Esperanza')

print('\n-Añadiendo la clave "Provincia":',dict_regions)

#F) Imprimir el diccionario nuevamente con las nuevas claves creadas.

print('\n-Imprimiendo todo el diccionario:',dict_regions)
print()