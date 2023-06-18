# 2. Utilizando ciclos se pide construya un programa que permita imprimir en la salida estándar
# la siguiente pirámide:

print()
# Decimo piso
print('         1')

# Noveno piso

print('        ',end='')
for i in range(2,4):
    print(i,end='')
print('2',end='')

#print('1',end='')

print('')

# Octavo piso

print('       ',end='')
for i in range(3,5):
    print(i,end='')
print('5',end='')

#print('1',end='')

for i in range(4,2,-1):
    print(i,end='')

print('')

# Septimo piso

print('      ',end='')
for i in range(4,7):
    print(i,end='')
print('7',end='')

#print('1',end='')

for i in range(6,3,-1):
    print(i,end='')

print('')

# Sexto piso

print('     ',end='')
for i in range(5,9):
    print(i,end='')
print('9',end='')

#print('1',end='')

for i in range(8,4,-1):
    print(i,end='')

print('')

# Quinto piso
print('    6789',end='')
for i in range(0,2):
    print(i,end='')

#print('1',end='')

for i in range(0,-1,-1):
    print(i,end='')
print('9876',end='')

print('')

# Cuarto piso
print('   789',end='')
for i in range(0,3):
    print(i,end='')

print('3',end='')

for i in range(2,-1,-1):
    print(i,end='')
print('987',end='')

print('')

# Tercer piso
print('  89',end='')
for i in range(0,5):
    print(i,end='')

print('5',end='')

for i in range(4,-1,-1):
    print(i,end='')
print('98',end='')

print('')

# Segundo piso
print(' 9',end='')
for i in range(0,7):
    print(i,end='')

print('7',end='')

for i in range(6,-1,-1):
    print(i,end='')
print('9',end='')

print('')

# Primer piso
for i in range(0,9):
    print(i,end='')

print('9',end='')

for i in range(8,-1,-1):
    print(i,end='')

print('\n')