#01-DATOS DE TIPO NUMERICO
estatura = 1.71 #Float
peso = 72 #Int
complejo = 1 +4j
edad= 28 #Int

#Impresion de la variable "estatura" y "peso"
print(f"Mi estatura es de {estatura} y mi peso es de {peso}")

#Impresion de un numero complejo
print("Impresion del numero complejo:", complejo)

#OPERACION ARITMETICA
imc = peso/estatura**2

print("Mi IMC es de: {:.2f}" .format(imc), "\n" )

#Transformando un entero a real
print("Transformando un valor real a entero:" ,int(peso))

#Transformando un real a entero
print("Transformando un valor entero a real:" ,float(edad))

#PRINT IMC
print("Mi indice de masa corporal es:",imc)

#02-DATOS DE TIPO CADENA DE CARACTERES
asignatura = "Programacion"
carrera = "Ingenieria Civil en Informatica"

print("La asignaruta de",asignatura,"corresponde a la carrera de",carrera)

#Utillizando la funcion len
print("La cantidad de caracteres de la palabra", asignatura, "es de:" ,len(asignatura))
print("La cantidad de caracteres de la palabra", asignatura, "es de:" ,len(carrera))

#03-VALORES BOLEANOS
ampolleta = False
interruptor = True

#Con type sabemos el tipo de  datos que estamos tratando
print(type(ampolleta))

#04-DATOS TIPO ARRAY (Objetos de Tipo Coleccion)
estudiantes = ["Matias", "Marco", "Cristobal", "Sebastian"]
num = [1,2,3,4,5,6]
print(estudiantes)
print(num)

#Declarando una lista
nueva_lista = list ()
print("Esta es una lista vacia:" ,nueva_lista)

otra_lista = []
print("Esta es otra lista:" ,otra_lista)
print(type(otra_lista))

#Declaramos otras listas
estudiantes = ["Matias", "Marco", "Cristobal", "Sebastian", "Marco"]
num = [1,2,3,4,5,6]
lenguaje = ["Phyton"]

#¿Se pueden realizar una lista de datos compuestos?
lista_compuesta = ["Matias", 28, True, 25.6]
print("Esta es la lista compuesta" ,lista_compuesta)

data = ["Osorno", {"UV": "nivel bajo" ,"temp °C": 18}, (-40.7464, -70.8383)]

print("Lista de cadenas de caracteres:", estudiantes)
print("Lista de numeros:", num)
print("Lista de un elemento:", lenguaje)
print("Esto igual es una lista:", data)
print(len(data)) #Cuenta elementos dentro de la lista
print(estudiantes.count("Marco")) #Cuenta ocurrencias

lenguaje = ["Javascript"]
print("Nuevo valor del arreglo de un elemento:" ,lenguaje)

#Acceder a un elemento especifico de la lista
print("Poscicion:", estudiantes[0]) #Primera poscicion de la lista
print("Poscicion:", estudiantes[1]) #Segunda posicion de la lista
#print("Poscicion:", estudiantes[5])
print("Poscicion -2:", estudiantes[-2]) #Desde atras hacia adelante

#Reasignar el valor de la posicion 3 de la lista
estudiantes[3] = "Gabriela"
print("El arreglo de estudiantes es:" ,estudiantes)

#Asigna valores de una lista a variables
data_asig = [10023, "Programacion",1,True]
cod,ramo,semestre,estado = data_asig
print(ramo)

#¿Se pueden sumar listas?
print("Suma de listas:" ,estudiantes + num)

#¿Que hace estas funciones?
print(list("Phyton"))
print(list(range(10)))
print("\n")




