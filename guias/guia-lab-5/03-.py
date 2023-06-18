# 3. Crear un algoritmo que permita saber si un año es bisiesto (calendario gregoriano)
# desde el ano 0 en adelante. Utilizar funciones para resolver el problema.

#=#=#=#=#=#=#=#=#=    INICIO    =#=#=#=#=#=#=#=#=#

def its_leap_year(year):
    if (year % 4 == 0) and (year % 100 != 0):
        return True
    elif year % 400 == 0:
        return True
    else:
        return False
    
def ask_year():
    while True:
        try:
            year = int(input('Ingresa un año: '))
            if year < 0:
                print('Ingresa un año mayor o igual a 0.')
                continue
            else:
                break
        except:
            print('Ingresa un numero valido.')
    return year


print('\n##### EJERCICIO 02 #####\n')

year = ask_year()

if its_leap_year(year):
    print(f'\nEl año {year} es bisiesto')
else:
    print(f'\nEl año {year} no es bisiesto')

print('\n##### FIN EJERCICIO #####\n')

#=#=#=#=#=#=#=#=#=#=    FIN    #=#=#=#=#=#=#=#=#=#=#

