
import os
#Ejemplo 1 Crear una lista de numeros e imprimir el contenido
numeros=[1,2,3,4,5]
print(numeros)

for i in numeros:
    print(i)

for i in range(0,len(numeros)):
    print(numeros[i])



os.system("cls")
#Ejemplo 2 Crear una lista de palabras y posteriormente buscar la coincidencia de una palabra
palabras=["hola","adios","mes","bye"]
buscar=input("Dame una palabra a buscar: ")

#1ra forma 
print(f"El numero de veces que se encontro la palabras: {palabras.count(buscar)}")
if buscar in palabras:
    print("Si encontro la palabra")
else:
    print("No encontro la palabra")    


#2da forma
encontro=False
for i in palabras:#En este for  i tiene el valor, no el indice
    if i==buscar:
        encontro=True

#3ra Forma
encontro=False
for i in range(0,len(palabras)): #En este for se controla mediante el indice 
    if palabras[i]==buscar:
        encontro=True



if encontro:
    print(f"Si encontro la palabra")
else:
    print(f"No encontro la palabra")

input("Oprima tecla...")



#Ejemplo 3 Añadir elementos a una lista
os.system("cls")
numeros=[]
print(numeros)
opc=True
while opc:
    numero=float(input("Dame un numero entero o decimal: "))
    numeros.append(numero)
    resp=input("Deseas agregar otro numero?").lower()
    if resp=="si":
        opc=True
    else:
        opc=False    

print(numeros)

input("Oprima tecla...")


#Ejemplo 4 crear una lista multidimensional que sea una agenda
agenda=[
        ["Carlos","6181234567"],
        ["Alberto","6661273654"],
        ["Martin","6185678923"],
       ]

for i in agenda: 
    print(i)

for r in range(0,3):
    for c in range(0,2):
        print(agenda[r])

cadena=""
for r in range(0,3):
    for c in range(0,2):
        cadena+=f"{agenda[r][c]},"
        
        

print(cadena)        