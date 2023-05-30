# 5. Crear 20 numeros, que se encuentren en el intervarlo 40 al 350 y los almacene en una
# lista y luego pida buscar algun numero dentro de los almacenados. Ademas que muestre
# la cantidad de ocurrencias de ese numero buscado.

#=#=#=#=#=#=#=#=#=    INICIO    =#=#=#=#=#=#=#=#=#

import random

# Inicia una lista que contendra los 20 numeros.
rand_list = []

# Escoje un numero al azar entre 40 y 450 y los añade a la lista.
for i in range (0, 20):
    random_num = random.randint(40, 350)
    rand_list.append(random_num)
#print(rand_list)

# Muestra en pantalla.
print('\n##### EJERCICIO 05 #####\n')

# Pide al usuario un numero.
while True:
    try:
        num_user = int(input('Ingrese un numero entre 40 y 350: '))
        if (num_user < 40) or (num_user > 350):
            print('Ingese un valor igual o mayor a 40.')
            continue
        else:
            break
    except ValueError:
        print('Ingese un numero valido.')

# Revisa si el numero esta en la lista, entonces imprimira sus ocurrencias.
if num_user not in rand_list:
    print('\nEl numero no se encuentra en la lista.')
else:
    ocurrencia = rand_list.count(num_user)
    print('\nEl numero se encuentra en la lista.')
    print('El numero aparece:', ocurrencia)

print('\n##### FIN EJERCICIO #####')

#=#=#=#=#=#=#=#=#=#=    FIN    #=#=#=#=#=#=#=#=#=#=#
