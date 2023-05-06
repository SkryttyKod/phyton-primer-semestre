print()
#01 - OPERADORES ARITMETICOS

print('########## OPERADORES ARITMETICOS ##########\n')

# Se declaran variables para proceder al uso de operadores.
a = 2
b = 6
c= 10
d = 30

# Operaciones comunes.
print("### 01 - Operaciones comunes ###\n")

print("suma entre dos números:", a + b) 
print("multiplicación entre dos números:", c*a)
print("Números elevados:", b**a)
print("Resta de números:", d - c)
print("División de números:", d/a,"\n")

# Operaciones con flotantes.
print("### 02 - Operaciones con flotantes ###\n")

# Tiempo y distancia.
T= 2
D = 6

# Por consecuencia.
V = T * D

#Operaciones con complejos.
print("### 02 - Operaciones con complejos ###\n")

c1 = 4 + 3j
print('La variable "c1" es de tipo: ',type(c1))

# Creando un número complejo con la funcion complex.
c2 = complex(3, -5) # 3 = Parte real | -5 = Parte imaginaria.
print("el numero complejo es:" ,c2,"\n")

print('La parte real de la var compleja "c1" es:',c2.real) #Se obtiene la parte real del número complejo
print('La parte imaginaria de la var compleja "c1" es:',c2.imag,'\n') #Se obtiene la parte imaginaria del número complejo

# ¿Se puede multiplicar un String con un número entero?
print("El verdadero texto sospechoso " * 3)

# ¿Y lo siguiente? (Da error).
# print("Hola" * 3.5 * 2)
# Si el resultado es 7 (número entero), ¿Por qué da error?
# R: No se pueden operar strings con numeros flotantes.

# ¿Y esta operación de suma?
print("Hola + 20") #Se puede pero solo con la función String.
print()

#02 - OPERADORES DE COMPARACION

print('########## OPERADORES ARITMETICOS ##########\n')

print('### 01 - Comparando numeros ###\n')

a = 1
b = 2
c = 3
d = 4

print ("¿a es igual que b?:",a == b)
print ("¿a es distinto que b?:",a != b)
print ("¿a es menor que b?:",a < b)
print ("¿b es menor que a?:",b < a)
print ("¿c es menor que d?:",c > d)
print ("¿c es menor que d?:",c < d,"\n")

print('### 02 - Comparando strings ###\n')

anim_dom = "perro"
anim_salv = "tigre"

# Compara los caracteres por orden alfabetico.
# Orden lexico de cada letra (valor numerico por letra = ASCII)
print(anim_dom == anim_salv)
print(anim_dom != anim_salv)
print(anim_dom > anim_salv)
print(anim_dom < anim_salv,'\n')

print('Comparando Numeros')

palabra = 'AAAA'
for ch in palabra:
    print(ch + ' = ' + str(ord(ch)))

palabra = 'aaaa'
for ch in palabra:
    print(ch + ' = ' + str(ord(ch)))

#03 - OPERADORES LOGICOS
print('\n########## OPERADORES LOGICOS ##########\n')

bencina = True
encendido = True
edad = 19

# Utilizando el opreador AND
if bencina and encendido:
    print('El vehiculo puede avanzar.')
else:
    print('El vehiculo no puede arrancar.')

# Utilizando operador OR
if bencina or encendido:
    print('El vehiculo puede avanzar.')
else:
    print('El vehiculo no puede arrancar.')

# Utilizando el operador NOT junto al AND
if not bencina and encendido:
    print('El vehiculo puede avanzar.')
else:
    print('El vehiculo no puede arrancar.')

# Utilizando el operador NOT junto al OR
if not bencina or encendido:
    print('El vehiculo puede avanzar.')
else:
    print('El vehiculo no puede arrancar.')

# Utilizando NOT junto AND y OR
if not bencina or (encendido and edad >= 18):
    print('El vehiculo puede arrancar.')
else:
    print('El vehiculo no puede arrancar.')
     


