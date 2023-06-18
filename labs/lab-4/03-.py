# 3. Se cuenta con dos sets: el primero contiene las temperaturas mínimas tomadas el mes de
# Mayo en Osorno. El segundo set contiene las temperaturas máximas: (40 Puntos)

# Temperaturas Mínimas = {9, 5, 2, 7, 6, 1}
# Temperaturas Máximas = {12, 14, 11, 10, 15, 9}

temp_min = {9, 5, 2, 7, 6, 1}
temp_max = {12, 14, 11, 10, 15, 9}
temp_union = {0}

temp_min_ele = []
temp_max_ele = []

# A) Verificar si la temperatura 9°C está en ambos sets

print()
if (9 in temp_min) and (9 in temp_max):
    print('El numero 9 esta en ambos sets')
else:
    print('El 9 no se encuentra en ambos sets')

# B) Comprobar si al menos la temperatura 6°C y 17°C está en alguno de los sets

print()
if (6 in temp_min or 17 in temp_min) or (6 in temp_max or 17 in temp_max):
    print('El numero 6 y 17 se encuentra en al menos algunos de los sets')
else:
    print('El 6 y 17 no se encuentra en algunos de los sets')

# C) Elevar a 4 todas las temperaturas dentro de los sets

# Temperaturas minimas.
for i in temp_min:
    temp_min_ele.append(i**2)
temp_min.clear()
for i in temp_min_ele:
    temp_min.add(i)

# Temperaturas maximas.
for i in temp_max:
    temp_max_ele.append(i**2)
temp_max.clear()
for i in temp_max_ele:
    temp_max.add(i)
    
# D) Unir ambos sets en uno solo
print()
union = temp_max_ele + temp_min_ele

temp_union.clear()

for i in union:
    temp_union.add(i)

print(temp_union)
print()



