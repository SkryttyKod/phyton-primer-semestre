# 2. Utilizar una funcion que permita ingresar nombres para que el usuario ingrese nombres
# uno por uno. Los nombres se deben almacenar en una lista. Luego, crear otra funcion
# que permita contar las letras, la cual debe recorrer la lista de nombres y cuente la cantidad 
# total de letras de todos los nombres ingresados. Por ultimo, crear una funcion para que 
# imprima los resultados y muestre en pantalla los nombres ingresados y el total de
# letras contadas.

#=#=#=#=#=#=#=#=#=    INICIO    =#=#=#=#=#=#=#=#=#

def enter_names():
    names_list_og = []
    names_list = []
    while True:
        user_name = input('Ingrese un nombre (o "exit" para terminar): ')
        name = user_name.replace(' ','')
        if name.lower() == 'exit':
            break
        elif name.lower() != 'exit' and name.lower().isalpha() : 
            names_list.append(name)
            names_list_og.append(user_name)
            continue
        else:
            print('Ingresa un nombre valido.')
            continue
    return names_list_og, names_list

def count_letters(name_list):
    count = 0
    for i in name_list:
        count += len(i)
    return count

def show_result(names_list_og, total_letters):
    print()
    print('Nombres ingresados:',', '.join(names_list_og))
    print('Total de letras contadas:', total_letters)

print('\n##### EJERCICIO 02 #####\n')

names_zip = enter_names()

names_list_og = names_zip[0]
names_list = names_zip[1]

total_letters = count_letters(names_list)
show_result(names_list_og, total_letters)

print('\n##### FIN EJERCICIO #####\n')

#=#=#=#=#=#=#=#=#=#=    FIN    #=#=#=#=#=#=#=#=#=#=#