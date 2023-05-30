# 3. Tres empleados de una fabrica trabajan en dos turnos: diurno y nocturno (10 hrs cada uno). Se busca calcular el pago diario y 
# el total semanal de cada empleado de acuerdo con los siguientes puntos:

# a) La tarifa de las horas diurnas es de 12000 CLP.
# b) La tarifa de las horas nocturnas es de 16000 CLP.
# c) Los domingos la tarifa se incrementa en 2000 CLP el turno diurno y 3000 CLP el turno nocturno.

#Ademas considerar:

#a) El primer empleado trabaja Lunes, Martes y Miercoles en turnos nocturnos, Jueves y Viernes en turnos diurnos.
# b) El segundo empleado trabaja Martes, Miercoles y Jueves turnos nocturnos, y tambien el dia domingo en turno diurno.
# c) El tercer empleado trabaja Miercoles, Jueves y Viernes diurno, Sabado y Domingo en turnos nocturnos.

# Guardar la informacion de cada empleado en un diccionario, con el pago diario que debe recibir cada empleado y el total de la semana.

#=#=#=#=#=#=#=#=#=    INICIO    =#=#=#=#=#=#=#=#=#

# Jornada diurna trabajada Lunes a Sabado
jor_diu = 12000 * 10

# Jornada nocturna trabajada Lunes a Sabado
jor_noc = 16000 * 10

# Jornada diurna trabajada un Domingo
jor_diu_dom = 14000 * 10

# Jornada nocturna trabajada Un Domingo
jor_noc_dom = 19000 * 10

# Iniciando diccionario del empleado 1
emp_1_info = {'Lunes'    : jor_noc,
              'Martes'   : jor_noc,
              'Miercoles': jor_noc,
              'Jueves'   : jor_diu,
              'Viernes'  : jor_diu,}

# Calculado ganancia semanal empleado 1
gan_sem_emp_1 = emp_1_info['Lunes'] + emp_1_info['Martes'] + emp_1_info['Miercoles'] + emp_1_info['Jueves'] + emp_1_info['Viernes']

# Iniciando diccionario del empleado 2
emp_2_info = {'Martes'    : jor_noc,
              'Miercoles' : jor_noc,
              'Jueves'    : jor_noc,
              'Domingo'   : jor_diu_dom,}

gan_sem_emp_2 = emp_2_info['Martes'] + emp_2_info['Miercoles'] + emp_2_info['Jueves'] + emp_2_info['Domingo']

# Iniciando diccionario del empleado 3
emp_3_info = {'Miercoles' : jor_diu,
              'Jueves'    : jor_diu,
              'Viernes'   : jor_diu,
              'Sabado'    : jor_noc,
              'Domingo'   : jor_noc_dom}

# Calculado ganancia semanal empleado 1
gan_sem_emp_3 = emp_3_info['Miercoles'] + emp_3_info['Jueves'] + emp_3_info['Viernes'] + emp_3_info['Sabado'] + emp_3_info['Domingo']


# Ubicando pagos semanales en cada diccionario.

emp_1_info['Pago semanal'] = gan_sem_emp_1
emp_2_info['Pago semanal'] = gan_sem_emp_2
emp_3_info['Pago semanal'] = gan_sem_emp_3

# Juntando los diccionarios.
dicc_final = {'Empleado 1' : emp_1_info,
              'Empleado 2' : emp_2_info,
              'Empleado 3' : emp_3_info}

# Mostrar en pantalla.
print('\n##### EJERCICIO 03 #####')
print()

for emp, info in dicc_final.items():
    print(emp.upper())
    for day, pay in info.items():
        print(day, ': ', pay, ' CLP', sep='')
    print()

print('Diccionario:')
print(dicc_final)

print('\n##### FIN EJERCICIO #####\n')

#=#=#=#=#=#=#=#=#=#=    FIN    #=#=#=#=#=#=#=#=#=#=#


