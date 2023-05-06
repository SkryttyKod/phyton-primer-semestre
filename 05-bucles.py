print()

print('########## BUCLES ##########\n')

edad = 15
num = 0

#while edad < 18:
#    print('Eres menor de edad, no puedes manejar')


print('### 01 - While ###')

# Mientras num sea igual o menor a 100, imprimira el num y
# luego cambiara el valor de num a +2 sobre el valor actual
# de num. Asi hasta que num sea = o mayor a 100.
while num <= 100:
    print(num)
    num = num + 2
print('Primer bucle terminado\n')

#Combinando while y else
while num <= 200:
    print(num)
    num += 2
else:
    print('Mi condicion es igual o mayor a 200')
print('Segundo bucle terminado.')

####