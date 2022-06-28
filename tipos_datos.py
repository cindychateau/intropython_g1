#Booleans
boolean = True #True o False

#Numerales
num = 10
fl = 10.34
nuevo_float = float(90) #Hace que el numero entero sea flotante
nuevo_entero = int(1092.33) #Hace que el numero flotante sea entero
print(nuevo_float)
print(nuevo_entero)

import random
num_aleatorio = random.randint(2, 5) #Número aleatorio entre 2 y 5
num_aleatorio_fl = random.uniform(1.5, 1.9) #Número aleatorio entre 1.5 y 1.9
print(num_aleatorio)

#Cadena o String
string = "ABCDEFG"
print("Este es el alfabeto", string) #La coma en automático me agrega un espacio
print("Este es el alfabeto "+string) #El + concatena los textos tal cual son
print("Este es un número", 10)
#print("Este es un número "+10) #ERROR estamos intentando sumar dos tipos de datos diferentes
print("Este es un número "+ str(10)) #str es transformar el número a que ahora sea cadena/string
print(f"Este es el alfabeto {string}") #Dentro de llaves ponemos la variable que queremos imprimir
print("El texto {}".format(string))

saludo = "hola mundo! bienvenidos a Python"
print(saludo.title()) #Primera letra de cada palabra sea mayúscula
print(saludo.upper()) #Todas las letras sean mayúsculas
print(saludo.lower()) #Todas las letras sean minúsculas
print(saludo.count('do')) #Regresa cuantos 'do' hay en el texto
print(saludo.split('o')) #Enlista y divide la cadena por cada 'o' que haya
print(saludo.find('Mundo')) #Devuelve dónde comienza 'mundo'. Regresa -1 si no lo encuentra

#Lista / Arreglo
lista_vacia = []
lista_llena = ["Hugo", "Paco", "Luis"] #0=> Hugo; 1=> Paco; 2=>Luis
print(lista_llena[0])
print(lista_llena[1])
print(lista_llena[2])
lista_llena[0] = "Donald"
print(lista_llena[0])
lista_llena.append("Mickey") #Agregamos un dato al final de la lista
print(lista_llena)
lista_llena.pop() #Elimina el último elemento de la lista
print(lista_llena)
lista_llena.pop(0) #Elimina el dato que indicamos entre paréntesis
print(lista_llena)
lista_mix = ["Cadena1", "Cadena2", 10, ["lista1.1", "lista1.2"]] #Las listas pueden ser de diferentes tipos de datos
lista_mix[3][0] = "NuevaLista"
print(lista_mix)
lista_nombres = ["Juana", "Pablo", "Pedro"]
nueva_lista = lista_mix+lista_nombres
print(nueva_lista)

#Diccionario (Objeto en JS)
diccionario_vacio = {}
diccionario = {"nombre": "Juana", "apellido": "De Arco", "edad": 30, "soltero": False}
print(diccionario)
print(diccionario["nombre"])
diccionario['estatura'] = 1.67
print(diccionario)
diccionario['hobbies'] = ["leer", "ver tele", "jugar"]
print(diccionario)
diccionario['nombre'] = "Elena"
print(diccionario)
nombre = diccionario.pop('nombre')
print(diccionario)
diccionario['name'] = nombre
print(diccionario)

#Tuplas -> NO se pueden modificar una vez que se le asigna un valor
tupla = ("A", "B", "C")
tupla2 = ("D", "E", "F")
print(tupla[0])