#Función es un bloque de código al cual nombramos y que podemos ejecutar constatemente
def hola():
    print("Hello World")

def holaReturn():
    print("ABC")
    sum = 1 + 2
    print(sum)
    return "Hello World Return"


hola()
hello = holaReturn() #hello = "Hello World Return"
print(holaReturn())

def suma(a, b): #a = 1; b = 2
    num_suma = a + b #num_suma = 1 + 2 -> 3
    print(num_suma) #IMPRESION 3

def sumaReturn(a, b):
    num_suma = a + b
    return num_suma

suma(1, 2)

sum = sumaReturn(3, 4)
print(sum)


def hello_world(nombre="John", apellido="Doe"): #nombre = "Elena"; apellido = "De Troya"
    frase = "Hola " +nombre+ " " +apellido #frase = "Hola Elena De Troya"
    return frase

variable_texto = hello_world("Elena") #variable_texto = "Hola Elena de Troya"
variable_texto = hello_world()
variable_texto = hello_world(apellido="De Troya")
print(variable_texto)

#Función que reciba una lista de números y que regrese la sumatoria de los números recibidos
#lista = [1, 2, 3, 4, 5]
#suma = 0
#num = 1
#suma += 1 -> 0 + 1 -> 1
#num = 2
#suma += 2 -> 1 + 2 -> 3
#num = 3
#suma += 3 -> 3 + 3 -> 6
#num = 4
#suma += 4 -> 6 + 4 -> 10
#num = 5
#suma += 5 -> 10 + 5 -> 15
def sumatoria(lista): 
    suma = 0
    for num in lista:
        suma += num

    return suma

suma = sumatoria([1, 2, 3, 4, 5]) # suma = 15



lista_num = [4, 5, 6, 7]
sum = sumatoria(lista_num)
print(sum)




#Función que reciba una lista de números y que me regrese el número MAYOR
#lista = [7, 8, 1, 2]
#num = 7
#n = 7
#n = 8
#num = 8
#n = 1
#n = 2
#RETURN 8
def num_mayor(lista):
    num = lista[0]
    for n in lista:
        if n > num:
            num = n
    return num

mayor = num_mayor([5,2,4,6]) #Me debe regresar 6
print(mayor)

lista_num = [7, 8, 1, 2]
mayor2 = num_mayor(lista_num) #Me debe regresar 8
print(mayor2)

#numero = 5
#lista = []
#i = 5
#lista = [5]
#i = 4
#lista = [5, 4]
#i = 3
#lista = [5, 4, 3]
#i = 2
#lista = [5, 4, 3, 2]
#i = 1
#lista = [5, 4, 3, 2, 1]
#i = 0
#lista = [5, 4, 3, 2, 1, 0]
def countdown(numero):
    lista = []
    for i in range(numero, -1, -1): #(Comienzo, Detenerse, Cantidad a avanzar)
        lista.append(i)
    return lista

print(countdown(5))

def imprimir_y_devolver(lista):
    print(lista[0])
    return lista[1]

print(imprimir_y_devolver([1,2]))

#lista = [1, 2, 7, 3]
#suma = 1 + 4 -> 5
#RETURN 5
def primero_mas_longitud(lista):
    suma = lista[0] + len(lista) #len(lista) nos regresa el tamaño de la lista/array
    return suma


pml = primero_mas_longitud([1, 2, 7, 3]) #pml = 5
print(pml)

#tamano = 3
#valor = 5
#lista = []
#i = 0
#lista = [5]
#i = 1
#lista = [5, 5]
#i = 2
#lista = [5, 5, 5]
#RETURN lista
def length_and_value(tamano, valor):
    lista = []
    for i in range(tamano): # 3
        lista.append(valor)
    return lista


lista_nueva = length_and_value(3, 5)
print(lista_nueva) 