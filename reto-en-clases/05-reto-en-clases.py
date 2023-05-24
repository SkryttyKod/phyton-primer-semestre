### 05 - RETO EN CLASES ###

# 5. Hacer un algoritmo que detecte si un número es par o impar, además si es un número primo y si es
# mayor o menor a 50. Para este ejercicio se solicita utilizar condicionales y bucles.

# 𝕀𝕟𝕚𝕔𝕚𝕠 𝕕𝕖𝕝 𝕣𝕖𝕥𝕠

while True:
    try:
        num = int(input('Ingrese un numero entero: '))
        if num < 0:
            print('Ingrese un numero positivo.')
        else:
            break
    except ValueError:
        print('Ingese un numero valido.')

if (num % 2) != 0:
    print('El numero', num, 'es: impar')
else:
    print('El numero', num, 'es: par')

if num < 50:
    print('El numero', num, 'es menor que 50')
elif num == 50:
    print('el numero', num, 'es igual que 50')
else:
    print('El numero', num, 'es mayor a 50')

divisores = []
divisores_comp = [1, num]

for i in range(1, num+1):
    if num % i == 0:
        divisores.append(i)

if divisores == divisores_comp:
    print('El numero es primo.')
else:
    print('El numero no es primo.')

# 𝔽𝕚𝕟 𝕕𝕖𝕝 𝕣𝕖𝕥𝕠