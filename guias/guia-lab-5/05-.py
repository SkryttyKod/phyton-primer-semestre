# 5. Desarrollar un programa que permita al usuario ingresar una serie de numeros enteros
# positivos (N numeros) hasta que ingrese -1 (Solo positivos ignorando los numeros negativos). 
# Luego, el programa debe calcular e imprimir en pantalla lo siguiente: el numero
# mayor de los ingresados, la sumatoria total de los numeros, la sumatoria de los numeros
# pares, la sumatoria de los numeros impares y el promedio total. Ademas, se debe imprimir si el numero 
# mayor obtenido es mayor, menor o igual que el promedio calculado.
# Asegurate de resolver este problema utilizando las funciones que consideres adecuadas.

# Nota: el -1 no se cuenta. Si el usuario ingresa un numero negativo debe volver a pedir un
# numero y no se usa en el calculo.

# Ejemplo: el usuario ingresa: 2, 3, 6, 7, 7, 9, -1 se debe imprimir en pantalla:
# La suma de pares es: 8
# La suma de impares es: 26
# La suma total es: 34
# El promedio es: 5
# El numero mayor ingresado fue: 9
# El numero es mayor que el promedio y este es 9

#=#=#=#=#=#=#=#=#=    INICIO    =#=#=#=#=#=#=#=#=#

def ask_nums():
    nums_list = []
    while True:
        try:
            user_num = int(input('Ingresa un numero (o "-1" para salir): '))
            if user_num == -1:
                break
            if user_num < 1:
                print('Ingresa un numero igual o mayor a 1.')
                continue
            else:
                nums_list.append(user_num)
        except:
            print('Ingresa un numero valido.')
    return nums_list

def calculating_things(num_list):
    sum_even = 0
    sum_odd = 0
    sum_all = sum(num_list)
    average = sum_all / len(num_list)
    num_max = max(num_list)
    for i in num_list:
        if i % 2 == 0:
            sum_even += i
        else:
            sum_odd += i
    return sum_even, sum_odd, sum_all, average, num_max

def show_screen(data):
    print('\nLa suma de pares es:', data[0])
    print('La suma de impares es:', data[1])
    print('La suma de todo es:', data[2])
    print('El promedio es:', data[3])
    print('El n° mayor ingresado es:', data[4])
    if data[3] > data[4]:
        print(f'El promedio es MAYOR que el numero mayor ingresado ({data[4]}).')
    elif data[3] < data[4]:
        print(f'El promedio es MENOR que el numero mayor ingresado ({data[4]}).')
    else:
        print(f'El promedio es IGUAL que el numero mayor ingresado ({data[4]}).')




print('\n##### EJERCICIO 02 #####\n')

show_screen(calculating_things(ask_nums()))

print('\n##### FIN EJERCICIO #####\n')

#=#=#=#=#=#=#=#=#=#=    FIN    #=#=#=#=#=#=#=#=#=#=#