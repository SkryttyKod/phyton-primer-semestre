print()
# 01 - CONDICIONALES

print('########## CONDICIONALES ##########\n')

licencia = False
edad = 19
auto = False

# Testeando comparadores.
print('### 01 - Testeando comparadores e IF ###\n')

if licencia:
    print('Puedo conducir porque tengo licencia')
else:
    print('No tengo licencia para conducir')
print("Este print esta fuera del else")

# Utilizando segundo condicional.
print('\n### 02 - Utilizando el segundo condicional IF ###\n')

if edad:
    print('Puedo conducir porque soy mayor de edad\n')
else:
    print('No puedo conducir soy menor de edad\n')


# Utilizando el tercer condicinal.
print('### 03 - Utilizando el tercer condicional IF ###')

if edad >= 18:
    print('Puedo conducir porque soy mayor de edad\n')
else:
    print('No puedo conducir soy menor de edad\n')

print('### 04 - Utilizando IF, ELIF y ELSE ###')
if licencia and edad >= 18:
    print('Puedo conducir porque soy mayor de edad y tengo licencia')
elif auto:
    print('Tengo automovil, pero no tengo licencia ni la edad necesaria')
else:
    print('No puedo conducir no tengo ni la edad, ni licencia ni automovil')