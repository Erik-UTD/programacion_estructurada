"""
List(Array)
son colecciones o conjunto de datos/valores bajo un mismo nombre, para acceder a los valores se hace como un indice numerico

Nota:Sus valores SI son modificables

La lista es una colección ordenada y modificable,
Permite miembros dubplicados

"""
import os
os.system
#Funciones más comunes en las LISTAS

paises=["México","Brasil","España","Canada"]

numeros=[23,12,100,34]

#Ordenar ascendemntemente
print(numeros)
numeros.sort()
print(numeros)
print(paises)
paises.sort()
print(paises)

#Añadir o Ingresar o Insertar elementos a una lista 

#1er forma
print(paises)
paises.append("Honduras")
#2da forma
paises.insert(1,"Honduras")
print(paises)

#Eliminar o Borrar o Quitar o Remover elementos de una lista
#1er forma (Con indice)
paises.pop(1)
print(paises)
#2da forma (Con el valor )
paises.remove("Honduras")

#Buscar un elemento dentro de una lista

#print("Brasil" in paises)

#1ra Forma
resp="Brasil" in paises

if resp:#if resp es lo mismo que if resp==True
    print("Si encontre el pais pedido")
else:
    print("No lo encontré")   


#2da Forma
pais_buscar=input("Dame el pais a buscar: ")
for i in range(0,len(paises)):
    if paises[i]==pais_buscar:
        print("Si encontré el país")
    else:
        print("No encontré el país")

#Cuántas veces aparace un elemento dentro de una lista
#numeros=[23,12,100,34]
print(f"Este numero 12 aparce: {numeros.count(12)} vez o veces")

numeros.append(12)
print(f"Este numero 12 aparce: {numeros.count(12)} vez o veces")


#Identificar o conocer el indice (posición) de un valor
#paises=["México","Brasil","España","Canada"]

indice=paises.index("España")
print(indice)
paises.pop(indice)
print(paises)


#Reccorrer los valores de una lista
#1ra forma con los valores
for i in paises:
    print(i)

#2da forma con los indices
for i in range(0,len(paises)):
    print(f"El valor {i} es: {paises[i]}")


#Unir contenido de listas 
#paises=["Mexico","Brasil","Canada"]
#numeros=[23,12,100,34,12]

print(paises)
print(numeros)
paises.extend(numeros)
print(paises)