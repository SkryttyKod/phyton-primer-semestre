# 7. Determinar el factorial de un numero n. donde:
# n! = n · (n − 1) · (n − 2)..,3 · 2 · 1 

#=#=#=#=#=#=#=#=#=    INICIO    =#=#=#=#=#=#=#=#=#

# Inicia variable factorial.
fact = 1
fact_list = []

# Muestra en pantalla.
print('\n##### EJERCICIO 07 #####\n')

# Piede un numero al usuario.
while True:
    try:
        user_num = int(input('Ingresa un numero entero: '))
        if user_num < 0:
            print('Ingresa un numero entero positivo.')
            continue
        else:
            break
    except:
        print('Ingresa un numero valido')

# Si el numero ingresado es 0.
if user_num == 0:
    print('El factorial de 0 es: 1')
    print('\n0! = 1')

# Si el numero es mayor a 0.
else:
    for i in range(1, user_num+1):
        fact = fact * i

    #formar la lista de factores.
    for j in range(user_num, 0, -1):
        j = str(j)
        fact_list.append(j)
    
    #Mostrar en pantalla.
    print('El factorial de', user_num, 'es:', fact)
    fact_list_str = ' * '.join(fact_list)
    print(f'\n{user_num}! = {fact_list_str} = {fact}')

print('\n##### FIN EJERCICIO #####\n')

#=#=#=#=#=#=#=#=#=#=    FIN    #=#=#=#=#=#=#=#=#=#=#

