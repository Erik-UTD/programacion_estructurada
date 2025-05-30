"""
Set.-
    Es un tipo de datos para tener una colección de valores pero no tiene ni indice ni orden

    Set es una coleccion desordenada, inmutable y no indexada.
    No hay miembros duplicados.
"""
import os
os.system("cls")

personas={"Ramiro","Choche","Lupe"}
print(personas)
personas.add("Peje")
print(personas)
personas.pop()
print(personas)
personas.clear()
print(personas)

varios={3.12,3,True,"hola"}
print(varios)

#Ejemplo Crear un programa que solicite los emails de los alumnos de a UTD almacenar en una lista y posteriormente mostrar en pantalla los emails sin duplicados
os.system("cls")
opc="si"
emails=[]
while opc=="si":
    emails.append(("dame el email: "))
    #print(emails)

    ipc=input("¿Deseas solicitar otro email(si/no)?").lower

#imprimir los email sin duplicados
print (emails)

#Convertir lista a set para que no haya duplicados
