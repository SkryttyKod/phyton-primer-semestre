# 3. Desarrollar un programa que al momento de ingresar los lados de un triangulo
# (a, b y c) en consola, indique si es equilatero, isosceles o escaleno. Tambien se
# solicita calcular el area utilizando la formula de Heron.

# ======== Variables ======== #
sides = []
is_triangle = None

# Titulo.
print('\n##### Identificador de Triangulos #####\n')

# ======== Ingreso de lados ======== #
for i in range(1, 4):
    sw = True
    while sw == True:
        try:
            side_entry = float(input(f'Ingrese el {i}° lado (u): '))
            if side_entry <= 0:
                print('Ingrese un numero valido.')
                continue
            else:
                sides.append(side_entry)
                sw = False
        except:
            print('Ingrese un numero valido.')

# ======== Revisa si los lados son validos ======== #
if (sides[0]+sides[1] > sides[2]) and (sides[1]+sides[2] > sides[0]) and (sides[0]+sides[2] > sides[1]):
    is_triangle = True
else:
    is_triangle = False

# ======== Formulas ======== #
p = (sides[0] + sides[1] + sides[2]) / 2
area = (p * (p - sides[0]) * (p - sides[1]) * (p - sides[2]))**0.5

# ======== Mostrar en pantalla ======== #
# Si es un triangulo.
if is_triangle == True:

    # Si es EQUILATERO.
    if (sides[0] == sides[1]) and (sides[0] == sides[2]) and (sides[1] == sides[2]):
        print('\nEl triangulo es EQUILATERO.')
        print('El area del triangulo es:', area,'u^2\n')
    
    # Si es ESCALENO.
    elif (sides[0] != sides[1]) and (sides[0] != sides[2]) and (sides[1] != sides[2]):
        print('\nEl triangulo es ESCALENO.')
        print('El area del triangulo es:', area,'u^2\n')
    
    # Si es ISOSCELES.
    else:
        print('\nEl triangulo es ISOSCELES.')
        print('El area del triangulo es:', round(area, 2),'u^2\n')

# Si no es un triangulo.
else:
    print('\nLos valores ingresados no corresponden a un triangulo.\n')




