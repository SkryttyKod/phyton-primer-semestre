### TIPO DE VARIABLES ###
print(" \n########## TIPO DE VARIABLES #########\n")

#00 - UN SIMPLE PRINT
print("### 00 - UN SIMPLE PRINT ###\n") #comentario
print("Hola soy Matias\n") #Funcion print

#01 - DECLARANDO VARIABLES
print("### 01 - DECLARANDO VARIABLES ###\n")

nombre = "Matias" #Variable "nombre" que tiene el valor de "Matias"
name = "Daniel" #Variable "name" que tiene el valor de "Daniel"
edad = 28 #Variable "edad" que tiene como valor el entero "28"

#02 - IMPRESION DE UNA VARIABLE
print("### 02- IMPRESION DE UNA VARIABLE ###\n")

print(nombre)
print(name)
print("Hola soy", name)
print("Hola soy", nombre)
print("Tengo", edad, "años de edad\n")

#03 - IMPRIMIENDO 2 VARIABLES EN UNA MISMA SENTENCIA (CONCADENACION)
print("### 03 - CONCADENACION ###\n")

print("Hola mi nombre es", nombre, "y tengo", edad, "años") #Uso de comas para la separacion
print("Hola mi nombre es " + nombre + " y tengo " + str(edad) + " años") #Uso de "+", ademas de la transformacion de la variable edad de "int" a "str"
print(f"Hola mi nombre es {nombre} y tengo {edad} años\n") #F-String (Cadena de formato):  Permite incrustar variables en una cadena de caracteres de manera más sencilla

#04 - ACTUALIZAR UNA VARIABLE (MUTABILIDAD)
print("### 04 - ACTUALIZACION DE UNA VARIABLE ###\n")

nombre = "Cris" #Se establece la variable "nombre" ("Matias") con el valor de "Cris"
print("Hola mi nuevo nombre es", nombre, "\n") #Imprimira el valor de la variable "nombre" actualizado como "Cris"

#05 - INSTRUCCION "INPUT"
print("### 05 - INTRUCCION INPUT ###\n")

nickname = input("¿Cual es tu nick?\n") #Realiza la pregunta y espera a que se ingrese una cadena de caracteres la cual sera el valor de la variable "nickname"
hrs_jug = int(input('¿Cuantas horas has jugado?\n')) #Transforma la entrada a un entero.
print("\nTu nickname es", nickname,'y has jugado durante',hrs_jug,'horas.' "\n")


