### 06 - FUNCIONES ###
print(" \n########## TIPO DE VARIABLES #########\n")

# Declarando funcoin simple
def mi_primera_funcion():
    print('Esta es mi primera funcion')

mi_primera_funcion()

def concatenar(lista1, lista2):
    return lista1 + lista2

lista1 = [1,2,3]
lista2 = [4,5,6]

print(concatenar(lista1, lista2))

def multiplicacion(num1, num2):
    return num1 * num2

print(multiplicacion(5,5))

def suma(a, b):
    return a+b

def resta(a, b):
    return a-b

a = int(input('Ingrese el valor de a: '))
b = int(input('Ingrese el valor de b: '))

resultado = suma(a, b)
print('La suma es de:', resultado)

resultado2 = resta(a, b)
print('La resta es de:', resultado2)