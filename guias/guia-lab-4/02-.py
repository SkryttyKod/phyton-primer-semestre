# 2. Construir un programa permita calcular e imprimir el resultado de la siguiente sumatoria:
# S = 500 + 456 + 510 + 454 + 520 + 452 + ... + 800 

#=#=#=#=#=#=#=#=#=    INICIO    =#=#=#=#=#=#=#=#=#

# Iniciando variables
sum_500_to_800 = 0
sum_456_to_398 = 0

# Recorre los numeros del 500 al 800 con un incremento de 10 y los va sumando.
for i in range(500, 801, 10):
    sum_500_to_800 += i

# Recorre los numeros del 456 al 398 con un decremento de 2 y los va sumando.
for i in range (456, 397, -2):
    sum_456_to_398 += i

# Suma todos los numeros
total = sum_500_to_800 + sum_456_to_398

# Muestra en pantalla.
print('\n##### EJERCICIO 02 #####')
print('\nS = 500 + 456 + 510 + 454 + 520 + 452 + ... + 800')
print('S =', total)
print('\n##### FIN EJERCICIO #####\n')

#=#=#=#=#=#=#=#=#=#=    FIN    #=#=#=#=#=#=#=#=#=#=#