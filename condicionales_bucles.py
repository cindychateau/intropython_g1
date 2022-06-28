#Condicionales
x = 20

if x > 10:
    print("Numero mayor a 10")
    print("Imprimos mas")
else:
    print("Numero menor a 10")


if x < 10:
    print("Menor a 10")
elif x < 15:
    print("Menor a 15")
else:
    print("Mayor")

if x > 10:
    print("Numero mayor")


#Bucles
for i in range(5): #0 - 4. ya NO entra el 5
    print(i)

print("------")

for i in range(1, 5): #1 - 4. Comenzamos en el primer número y entra el bucle siempre y cuando sea menor al 2do numero
    print(i)

print("------")

for i in range(0, 10, 3): #(Comienzo, Detenerse, Cantidad a avanzar)
    print(i)


string = "Buenos días"
for x in string:
    print(x)

array = ['A', 'B', 'C', 'D']
for letra in array: #letra = 'A'; letra = 'B'; letra = 'C'; letra = 'D'
    print(letra)

diccionario = {"nombre": "Juana", "apellido": "De Arco", "edad": 30}
for atributo in diccionario: #atributo = nombre; atributo = apellido; atributo = edad
    print(diccionario[atributo])

y = 0
while y < 3:
    print(y)
    y += 1 


print("-------")

#BREAK -> es una interrupción al bucle. Deja de ejecutar el bucle, SALE del bucle
#CONTINUE -> es una interrupción a esa ronda del bucle. El bucle ignora esa ronda y continúa a la siguiente ronda

#Dado un for comenzando en 1 y hasta el 15, IMPRIME todos los numeros EXCEPTO aquellos múltiples de 5
# % ->restante
for n in range(1, 16): #n = 1
    if n % 5 == 0: #Multiple de 5
        continue 
    print(n)

#Dada una cadena, imprime cada uno de los caracteres y DETENTE cuando encuentres un .
cadena1 = "Había una vez. Un pajarito"
for letra in cadena1:
    if letra == ".":
        break
    
    print(letra)
