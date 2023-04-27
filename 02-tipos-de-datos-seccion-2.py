######### TIPOS DE DATOS #########
print("#### TIPOS DE DATOS ####\n")

#01 - DATOS DE TIPOS NUMERICOS
print("### 01 - DATOS DE TIPOS NUMERICOS ###\n")

edad = 28 #Entero (Int)
estatura = 1.71 #Real (Float)
peso = 72.5 
complejo = 1 + 4j #Complejo (Complex)

print(f"Mi edad es {edad}, mi estatura es {estatura}, mi peso es {peso}\n")

#Transformando un real a entero
print(peso)
print("Transformando un valor real a un entero:",int(peso),"\n")

#Transformando un entero a flotante
print(edad)
print("Transformando un valor real a un entero:",float(edad),"\n")

#OPERACIONES ARITMETICAS BASICA
print("### Operaciones aritmeticas basicas ###\n")
imc = peso / (estatura**2)
print("Mi IMC es de: ",imc,"")
print("Mi IMC es de: {:.2f}".format(imc),"\n") #Formateado.

#02 - TIPOS DE DATOS CADENA DE CARACTERES
print("### 02 - TIPOS DE DATOS CADENA DE CARACTERES ###\n")

asignatura = "Programación"
carrera = "Ingenieria Civil en Informatica"
print("############# 02 - STRINGS #############")
print(f"La asignatura de {asignatura}, corresponde a la carrera de {carrera}.")

#Utilizando la funcion len (cuenta de caracteres).
print(f"La cantidad de caracteres de la palabra {asignatura} es de:",len(asignatura))
print(f"La cantidad de caracteres de la palabra {carrera} es de:",len(carrera),"\n")

#03 - VALORES BOOLEANOS
ampolleta = False
interruptor = True
print("########## 03 - BOOLEANS ##########")
print(ampolleta,interruptor)
print("La variable ampolleta es de tipo:",type(interruptor),"\n") #Funcion type para saber el tipo de dato.

#Podemos transformar cualquier valor a un Booleano (al igual que un string.)
print(bool(0))
print(bool(""))
print(bool(None))
print(bool("True"))
print(bool(1))
print(bool("\n"),"\n")

#04 - LISTAS
print("###### 04 - LISTAS ######\n")

#Iniciando lista de dos maneras.
nueva_lista = list()
otra_lista = []

print("Esta es una lista vacia:",nueva_lista)
print("Esta es otra lista vacia",otra_lista)
print(type(otra_lista),"\n")

#declarando 3 listas diferentes.
estudiantes = ["Matias", "Marco", "Cristobal", "Sebastian", "Marco"]
num = [1,1,2,3,4,5,6]
lenguaje = ["Phyton"]

#¿Se puede realizar una lista de datos compuestos?
data = ['Osorno', {'UV': 'Nivel bajo', 'Temp °C': '15' }, (-40,5725, -73.1353)]
lista_mixta = ["Franco", 10, True]


print("Lista de cadena de caracteres:", estudiantes)
print("Lista de numeros:", num)
print("Lista de un elemento", lenguaje)
print("Esto es una lista mixta:", lista_mixta)
print("Esto igual es una lista:", data, "\n")
print("La lista tiene:", len(lista_mixta),"elementos.") #Saber la cantidad de elemento en la lista.
print("La cantidad de veces que se repite Marco es:", estudiantes.count("Marco")) #Cantidad de ocurriencias de un elemento de una lista.
print("La cantidad de veces que se repite el n° 1 es:", num.count(1),"\n")

lenguaje = ['Javascript']
print("Nuevo valor del arreglo de un elemento:",lenguaje,"\n")

# ¿Como accedo a un elemento especficio de la lista? (### INDEX/POSICION/INDICES ###)
print(estudiantes[0]) # Correcto (1° elemento de la lista).
print(estudiantes[1]) # Correcto (2° elemento de la lista).
#print(estudiantes[5]) # Incorrecto / Esta fuera del rango.
print("Poscion -2:", estudiantes[-2]) # Cuenta desde atras hacia adelante.






























print()