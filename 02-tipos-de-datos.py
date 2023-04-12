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

print("La variable \"ampolleta\" es de tipo:", type(ampolleta), "\n") #Type para saber el tipo de variable.
print("La variable \"estatura\" es de tipo:", type(estatura)) #Type para saber el tipo de variable.
print("La variable \"peso\" es de tipo:", type(peso)) #Type para saber el tipo de variable.
print("La variable \"complejo\" es de tipo:", type(complejo))  #Type para saber el tipo de variable.
print("La variable \"carrera\" es de tipo:", type(carrera), "\n")  #Type para saber el tipo de variable.

#03 - DATOS DE TIPO ARRAY (Objetos de Tipo Coleccion)
print("### 04 - DATOS DE TIPO ARRAY ###\n")

estudiantes = ["Matias", "Marco", "Cristobal", "Sebastian"] #Inicia una variable como una lista de elementos str.
num = [1,2,3,4,5,6] #Inicia una variable como una lista de elementos int.
print("Los estudiantes son:", estudiantes) #Imprime la variable "estudiantes" que es una lista.
print("Los numeros de un dado son:", num, "\n") #Imprime la variable "num" que es una lista.

nueva_lista = list () #Inicia una lista vacia.
print("Esta es una lista vacia:" ,nueva_lista) #Imprime la lista vacia.

otra_lista = [] #Inicia otra lista vacia.
print("Esta es otra lista:" ,otra_lista) #Imprime otra lista vacia.
print("La variable \"nueva_lista\" es de tipo:", type(nueva_lista))
print("La variable \"otra_lista\" es de tipo:", type(otra_lista), "\n")

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
print("¿Cuantas veces esta \"Raul\" en la lista \"grupo\"?", grupo.count("Raul"), "\n") #Cuenta ocurrencias.

lenguaje = ["Javascript"] #Establece el elemento de la variable "lenguaje" en "Javascript" (Antes "Phyton").
print("Nuevo valor del arreglo de un elemento:" ,lenguaje, "\n")

#Acceder a un elemento especifico de la lista
print("Poscicion 1:", estudiantes[0]) #Accede a la primera poscicion de la lista "estudiantes".
print("Poscicion 2:", grupo[1]) #Accede a la segunda posicion de la lista "grupo".
#print("Poscicion:", estudiantes[5])
print("Poscicion -2:", estudiantes[-2], "\n") #Accede a la segunda poscicion de la lista "estudiantes", desde atras hacia adelante.

estudiantes[3] = "Gabriela" #Reasigna el valor de un elemento de la lista.
print("El arreglo de estudiantes es:" ,estudiantes)

#Asigna valores de una lista a variables
data_asig = [10023, "Programacion",1,True]
cod,ramo,semestre,estado = data_asig
print(ramo)

#¿Se pueden sumar listas?
print("Suma de listas:" ,estudiantes + num)

#¿Que hace estas funciones?
print(list("Phyton")) #Transforma el str "Phyton" en una lista.
print(list(range(10))) #Imprime una lista de rango 10 (0-9)
print("\n") #Salto de linea



