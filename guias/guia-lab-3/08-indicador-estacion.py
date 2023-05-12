# 8. Elaborar un algoritmo que permita al usuario ingresar un mes y arroje la estacion
# correspondiente a ese mes: verano, otoño, invierno o primavera.

# ======== Listas ======== #
months = ['enero', 'febrero', 'marzo', 'abril',
          'mayo', 'junio', 'julio', 'agosto',
          'septiembre', 'octubre', 'noviembre', 'diciembre']

seasons = ['Verano', 'Otoño', 'Invierno', 'Primavera']

# Titulo.
print ('\n##### Averigua la estacion #####\n')

# ======== Ingreso del mes ======== #

while True:
    month_input = input('Ingresa el mes: ')
    month_user = month_input.lower()
    month_user_c = month_input.capitalize()

    # Verifica si el mes ingresado es valido.
    if month_user in months:

        if (month_user == 'enero') or (month_user == 'febrero'):
            print('\nEl mes de ', month_user_c, ' cae en:\n', seasons[0], ' (21 Dic. - 20 Mar.).\n', sep='')

        elif (month_user == 'abril') or (month_user == 'mayo'):
            print('\nEl mes de ', month_user_c, ' cae en:\n', seasons[1], ' (21 Mar. - 20 Jun.).\n', sep='')

        elif (month_user == 'julio') or (month_user == 'agosto'):
            print('\nEl mes de ', month_user_c, ' cae en:\n', seasons[2], ' (21 Jun. - 20 Sep.).\n', sep='')

        elif (month_user == 'octubre') or (month_user == 'noviembre'):
            print('\nEl mes de ', month_user_c, ' cae en:\n', seasons[3], ' (21 Mar. - 20 Jun.).\n', sep='')

        elif (month_user == 'diciembre'):
            print('\nEl mes de ', month_user_c, ' cae en:\n', seasons[0], ' (21 Dic. en adelante).\n', seasons[3], ' (20 Dic. hacia atras).\n', sep='')
        
        elif (month_user == 'marzo'):
            print('\nEl mes de ', month_user_c, ' cae en:\n', seasons[1], ' (21 Mar. en adelante).\n', seasons[0], ' (20 Mar. hacia atras).\n', sep='')

        elif (month_user == 'junio'):
            print('\nEl mes de ', month_user_c, ' cae en:\n', seasons[2], ' (21 Jun. en adelante).\n', seasons[1], ' (20 Jun. hacia atras).\n', sep='')
        
        elif (month_user == 'septiembre'):
            print('\nEl mes de ', month_user_c, ' cae en:\n', seasons[3], ' (21 Sep. en adelante).\n', seasons[2], ' (20 Sep. hacia atras).\n', sep='')
        
        break
    else:
        print('Mes ingresado invalido.')

