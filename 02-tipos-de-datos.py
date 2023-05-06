### TIPOS DE DATOS ###
print(" \n########## TIPO DE DATOS #########\n")

#01 - DATOS DE TIPO NUMERICO
print("### 01 - DATOS DE TIPO NUMERICO ###\n")

estatura = 1.71 #Tipo "Float". Aquellos que pueden contener una parte decimal.
peso = 72 #Tipo "Int". Son los numeros enteros sin parte decimal.
edad = 27

#Tipo "Complex". Son numeros complejos Se declaran usando la "j" para la parte imaginaria.
#La variable "complejo" tendra el valor "1 + 4i". Tambien se declaran: z = complex(2, 3)
complejo = 1 + 4j

print(f"Mi estatura es de {estatura} m y mi peso es de {peso} Kg") #Impresion de la variable "estatura" y "peso" en un f-string.
print("Impresion del numero complejo:", complejo) #Impresion de un numero complejo.

imc = peso/estatura**2 #Operacion aritmetica. Dividir la variable "peso" entre "estatura" al cuadrado. El resultado se guarda en la variable "imc"
print("Mi indice de Masa Corporal es:",imc)
print("Mi IMC es de: {:.2f}" .format(imc), "\n" ) #Impresion con formato. "{:.2f}" Indica que se usaran 2 decimales. ".format(imc)" Inserta la variable "imc" al string

#Transformando un numero real en un numero entero (int).
print("Transformando un valor real a entero:" ,int(estatura))

#Transformando un numero entero en un numero real (float).
print("Transformando un valor entero a real:" ,float(edad), "\n")

#02 - DATOS DE TIPO CADENA DE CARACTERES
print("### 02 - DATOS DE TIPO CADENA DE CARACTERES ###\n")

asignatura = "Programacion"
carrera = "Ingenieria Civil en Informatica"

print("La asignaruta de", asignatura, "corresponde a la carrera de", carrera, "\n") #Impresion de las variables "asignatura" y "carrera".

#Utillizando la funcion len.
print("La cantidad de caracteres de la palabra", asignatura, "es de:" ,len(asignatura)) #Cuenta los caracteres de la variable "asignatura".
print("La cantidad de caracteres de la palabra", asignatura, "es de:" ,len(carrera), "\n") #Cuenta los caracteres de la variable "carrera". Incluye espacios.

#03 - DATOS DE TIPO BOLEANOS
print("### 03 - DATOS DE TIPO BOLEANOS ###\n")

ampolleta = False #La variable "ampolleta" esta encendida.
interruptor = True #La variable "interruptor" esta apagada.

print("La variable \"ampolleta\" es de tipo:", type(ampolleta)) #Type para saber el tipo de variable.
print("La variable \"estatura\" es de tipo:", type(estatura)) #Type para saber el tipo de variable.
print("La variable \"peso\" es de tipo:", type(peso)) #Type para saber el tipo de variable.
print("La variable \"complejo\" es de tipo:", type(complejo))  #Type para saber el tipo de variable.
print("La variable \"carrera\" es de tipo:", type(carrera), "\n")  #Type para saber el tipo de variable.

#04 - DATOS DE TIPO ARRAY (Objetos de Tipo Coleccion)
print("### 04 - DATOS DE TIPO LISTAS ###\n")

estudiantes = ["Matias", "Marco", "Cristobal", "Sebastian"] #Inicia una variable como una lista de elementos str.
num = [1,2,3,4,5,6] #Inicia una variable como una lista de elementos int.
print("Los estudiantes son:", estudiantes) #Imprime la variable "estudiantes" que es una lista.
print("Los numeros de un dado son:", num, "\n") #Imprime la variable "num" que es una lista.

empty_list = list() #Inicia una lista vacia.
print("Esta es una lista vacia:" ,empty_list) #Imprime la lista vacia.

other_empty_list = [] #Inicia otra lista vacia.
print("Esta es otra lista vacia:" ,other_empty_list) #Imprime otra lista vacia.
print("La variable \"empty_list\" es de tipo:", type(empty_list))
print("La variable \"other_empty_list\" es de tipo:", type(other_empty_list), "\n")

#Declaramos otras listas.
grupo = ["Priscilla", "Raul", "Mariana", "Renato", "Raul"]
numeros = [1,2,3,4,5,6]
lenguaje = ["Phyton"]

#¿Se pueden realizar una lista de datos compuestos?
lista_compuesta = ["Matias", 28, True, 25.6]
data = ["Osorno", {"UV": "nivel bajo" ,"temp °C": 18}, (-40.7464, -70.8383)] #Diccionarios
print("Esta es la lista compuesta: ", lista_compuesta)
print("Esta es la otra lista compuesta: ", data, "\n")

print("Esta es una lista de cadenas de caracteres:", estudiantes)
print("Esta es una lista de numeros:", num)
print("Esta es una lista de un elemento:", lenguaje)
print("Esto igual es una lista:", data, "\n")

print("El numero de elementos en la lista \"data\" es de:", len(data)) #Cuenta elementos dentro de la lista.
print("¿Cuantas veces esta \"Raul\" en la lista \"grupo\"?", grupo.count("Mariana"), "\n") #Cuenta ocurrencias.

lenguaje = ["Javascript"] #Establece el elemento de la variable "lenguaje" en "Javascript" (Antes "Phyton").
print("Nuevo valor del arreglo de un elemento:" ,lenguaje, "\n")

#Acceder a un elemento especifico de la lista
print("Poscicion 1 en la lista \"estudiantes\":", estudiantes[0]) #Accede a la primera poscicion de la lista "estudiantes".
print("Poscicion 2 en la lista \"grupo\":", grupo[1]) #Accede a la segunda posicion de la lista "grupo".
#print("Poscicion:", estudiantes[5])
print("Poscicion -2 en la lista \"estudiantes\":", estudiantes[-2], "\n") #Accede a la segunda poscicion de la lista "estudiantes", desde atras hacia adelante.

estudiantes[3] = "Gabriela" #Reasigna el valor de un elemento de la lista.
print("El arreglo de estudiantes es:" ,estudiantes)

#Asigna valores de una lista a variables
data_asig = [10023, "Programacion", 1, True]
cod,ramo,semestre,estado = data_asig
print('Codigo:',cod)
print('Ramo:',ramo)
print('Semestre:',semestre)
print('Estado:',estado)

#¿Se pueden sumar listas?
print("\nSuma de listas:" ,estudiantes + num)

#¿Que hace estas funciones?
print(list("Phyton")) #Transforma el str "Phyton" en una lista.
print(list(range(10))) #Imprime una lista de rango 10 (0-9)
print("\n") #Salto de linea

#05 - DATO DE TIPO TUPLAS
print("### 05 - DATOS DE TIPO TUPLAS ###\n")

grupo1 = ("Daniel", "Cristian", "Felipe", 200, 100, "Daniel")
print("La variable \"grupo1\" es de tipo:", type(grupo1))

grupo2 = ("Diego", "Boris", "2020", "Alberto", "100", "Pedro")

#Accediendo al primer elemento de la tupla.
print('El elemento 1 de "grupo1" es:',grupo1[0])

#Consultando el elemento Daniel cuantas veces se encuentra en la tupla
print("El elemento \"Daniel\" se repite:", grupo1.count("Daniel"), "veces")

#Muestra el indice del primer elemento buscado
print("El indice del elemento \"Daniel\" es:", grupo1.index("Daniel"))

#Reasignando el primer elemento de la tupla
#grupo1[0] = "Constanza" #Las tuplas no aceptan asignacion de elementos.
#print(grupo1)

#Se pueden sumar las tuplas
print("Suma de tuplas:", grupo1 + grupo2)

#Obteniedo un trozo de la tupla
print("Trozo de la tupla:", grupo2[0:3])

#¿Entonces como no puedo modificar una tupla?
grupo1 = list(grupo1)
print("La tupla ahora es de tipo:", type(grupo1), "\n")

#06 - SETS (Conjuntos) - Estructura fija de datos.
print("### 06 - DATOS DE TIPO SETS ###\n")

conjunto_vacio = set()
conjunto_vacio1 = {}
conjunto_colores = set({"Azul", "Rojo", "Verde"})
conjunto_animales = {"Gato", "Perro", "Loro"}

print("\"conjuto_colores\" es de tipo:", type(conjunto_colores))
print("\"conjuto_vacio1\" es de tipo:", type(conjunto_vacio1))
print("\"conjuto_colores\" es de tipo:", type(conjunto_colores))
print("\"conjuto_animales\" es de tipo:", type(conjunto_animales), "\n")

#print(conjunto_animales[0]) #Accediendo al primer elemento del set
conjunto_colores.add("Celeste")
print("El set de colores lo conforman:", conjunto_colores)

conjunto_animales.add("Gato")
print("El set de animales lo conforman:", conjunto_animales, "\n")

#07 - DICCIONARIOS (Clave-Valor)
print("### 06 - DATOS DE TIPO DICCIONARIO ###\n")
print('Prueba de que funciona: ')
diccionario={
    "Nombre":"Pepe",
    "Institucion":"Escuela",
    "Edad":4,
    "colores": {"rojo","azul"}
}
print(diccionario)
print(
    "hola "
    "esto es una "
    "prueba"
)
 #Actualizar valor de un diccionario.
print(diccionario["Nombre"])
diccionario["Nombre"]= "Matias"
print(diccionario)

#Eliminando campo de un diccionario.
del diccionario["Nombre"]
print(diccionario)





