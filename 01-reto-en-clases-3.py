##### reto en clases 3 #####

city_list = ['Santiago', 'Temuco', 'Osorno', 'Punta arenas']
ica_list = [134, 99, 245, 50]

ica_min = min(ica_list)
city_min = city_list[ica_list.index(ica_min)]

ica_max = max(ica_list)
city_max = city_list[ica_list.index(ica_max)]

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







print(city_min,':',ica_min)
print(city_max,':',ica_max)


