# 4. Desarrollar un algoritmo que permita devolver la siguiente propiedad descubierta por Nicomaco de Gerasa:

# Sumando el primer impar, se obtiene el primer cubo.
# Sumando los dos siguientes impares, se obtiene el segundo cubo
# Sumando los tres siguientes, se obtiene el tercer cubo, y asi sucesivamente.
# Ejemplo:

# 1**3 = 1 = 1
# 2**3 = 3 + 5 = 8
# 3**3 = 7 + 9 + 11 = 27
# 4**3 = 13 * 15 * 17 * 19 = 64

# Imprimir por pantalla, los primeros n cubos, considerando el valor de n obtenido desde teclado.

#=#=#=#=#=#=#=#=#=    INICIO    =#=#=#=#=#=#=#=#=#

print('\n##### EJERCICIO 04 #####\n')

# Pide un numero al usuario.
while True:
    try:
        num_user = int(input('Ingrese un numero entero: '))
        if num_user < 1:
            print('Ingese un valor igual o mayor a 1.')
            continue
        else:
            break
    except ValueError:
        print('Ingese un numero valido.')
print()

# Gestiona la impresion de las lineas
odd = 1
for i in range(num_user):
    odd_list = []
    odd_sum = 0
    j = 0

    # Realiza los calculos que se imprimiran por linea.
    while j <= i:
        odd_sum += odd
        odd_list.append(str(odd))
        odd += 2
        j += 1

    odd_str = ' + '.join(odd_list)

    print(f'{i+1}**3 = {odd_sum} ➜  {odd_str} = {odd_sum}')

print('\n##### FIN EJERCICIO #####\n')

#=#=#=#=#=#=#=#=#=#=    FIN    #=#=#=#=#=#=#=#=#=#=#

