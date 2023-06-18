# 1. Realizar un programa donde el usuario indique la cantidad de numeros que va a ingresar,
# luego solicitar dicha cantidad de numeros e imprimir en pantalla, la suma de todos estos 
# numeros, la suma de los pares y la suma de los impares. Se debe resolver utilizando
# funciones para cada una de las operaciones mencionadas anteriormente.

#=#=#=#=#=#=#=#=#=    INICIO    =#=#=#=#=#=#=#=#=#

def ask_cant_nums():
    print('\n##### EJERCICIO 01 #####\n')
    while True:
        try:
            cant_nums = int(input('Ingrese la cantidad de numeros que ingresará: '))
            if cant_nums < 1:
                print('Ingresa un numero igual o mayor a 1.')
                continue
            else:
                break
        except:
            print('Ingrese un numero valido.')
    return cant_nums

def ask_nums(amount):
    user_num_list = []
    for i in range(amount):
        while True:
            try:
                user_num = int(input('Ingresa un numero: '))
                user_num_list.append(user_num)
                break
            except:
                print('Ingrese un numero valido.')
    return user_num_list

def sum_all_even_odd(num_list):
    sum_even = 0
    sum_odd = 0
    sum_all = sum(num_list)
    for i in num_list:
        if i % 2 == 0:
            sum_even += i
        else:
            sum_odd += i
    return sum_even, sum_odd, sum_all

def show_result(user_num_list, sums):
    print('\nNumeros ingresados:')
    print(user_num_list, '\n')
    print('Suma N° pares:', sums[0])
    print('Suma N° impares:', sums[1])
    print('Suma total:', sums[2])
    print('\n##### FIN EJERCICIO #####\n')

cant_nums = ask_cant_nums()
user_num_list = ask_nums(cant_nums)
sums = sum_all_even_odd(user_num_list)

show_result(user_num_list, sums)

#=#=#=#=#=#=#=#=#=#=    FIN    #=#=#=#=#=#=#=#=#=#=#

