### 03 - RETO EN CLASES ###

# Escriba un programa que incluya una lista de nombres de ciudades en Chile y una lista de índices de calidad del aire (ICA),
# para cada ciudad. El programa debe determinar el nombre de la ciudad con el índice de calidad del aire más bajo y 
# el nombre de la ciudad con el índice de calidad del aire más alto. Luego, para cada ciudad, el programa debe imprimir un 
# mensaje que indique el nivel de calidad del aire de la ciudad en función de los siguientes criterios:

# Si el ICA está entre 0 y 50, el nivel de calidad del aire se considera BUENO.
# Si el ICA está entre 51 y 100, el nivel de calidad del aire se considera MODERADO.
# Si el ICA está entre 101 y 150, el nivel de calidad del aire se considera DAÑINO PARA LA SALUD DE GRUPOS SENSIBLES.
# Si el ICA está entre 151 y 200, el nivel de calidad del aire se considera DAÑINO PARA LA SALUD.
# Si el ICA está entre 201 y 300, el nivel de calidad del aire se considera MUY DAÑINO PARA LA SALUD.
# Si el ICA es mayor que 300, el nivel de calidad del aire se considera PELIGROSO.

### 𝕀𝕟𝕚𝕔𝕚𝕠 𝕕𝕖𝕝 𝕣𝕖𝕥𝕠 ###

# Inicia las listas que contienen las ciudades y el ica.
city_list = ['Santiago', 'Temuco', 'Osorno', 'Punta arenas']
ica_list = [134, 99, 245, 50]

# Para la ciudad con el valor de ica menor.

# Extrae el valor menor de la lista "ica_list" y lo asigna a la var "ica_min"
# Luego "city min" toma como valor el elemento en la posicion correspondiente a
# "ica_min" de la lista "ica_list"
ica_min = min(ica_list)
city_min = city_list[ica_list.index(ica_min)]

# Lo mismo pero con los valores mayores
ica_max = max(ica_list)
city_max = city_list[ica_list.index(ica_max)]

# Recorre los datos para comprobar los rangos e imprimir su rango de ica.
for i in range (len(city_list)):
    if ica_list[i] >= 0 and ica_list[i] <= 50:
        print(city_list[i], 'Tiene un indice de calidad BUENO.')
    elif ica_list[i] >= 51 and ica_list[i] <= 100:
        print(city_list[i], 'Tiene un indice de calidad MODERADO.')
    elif ica_list[i] >= 101 and ica_list[i] <= 150:
        print(city_list[i], 'Tiene un indice de calidad DAÑINA PARA LA SALUD GRUPOS SENSIBLEs.')
    elif ica_list[i] >= 151 and ica_list[i] <= 200:
        print(city_list[i], 'Tiene un indice de calidad DAÑINA PARA LA SALUD.')
    elif ica_list[i] >= 201 and ica_list[i] <= 300:
        print(city_list[i], 'Tiene un indice de calidad MUY DAÑINA PARA LA SALUD.')
    else:
        print(city_list[i], 'Tiene un indice de calidad PELIGROSA.')

# Imprime los valores minimos-maximos y las ciudades correspondientes.
print(city_min,':',ica_min)
print(city_max,':',ica_max)

### 𝔽𝕚𝕟 𝕕𝕖𝕝 𝕣𝕖𝕥𝕠 ###