"""
dict.-
Es un tipo de datos que se utiliza para alamacenar datos de diferente tipo de datos pero en lugar de tener como las listas indices numericos tiene alfanumericos. Es decir es algo paredico como los Objetos.

Tambien se conoce como un arreglo asosiativo u Objeto JSON

El diccionario es una colección ordenada ** y modificable. No hay miembros duplicados.
"""
import os
os.system("cls")

#Lista
#paises=["Mexico","Brasil","Canadá","España"]

#dict u objeto
pais_mexico={"nombre":"México",
        "capital":"CDMEX",
        "poblacion":"12000000",
        "idioma":"español",
        "status":True
        }

pais_brasil={"nombre":"Brasil",
        "capital":"Brasilia",
        "poblacion":"10000000",
        "idioma":"portugues",
        "status":True
        }


pais_canada={"nombre":"Canada",
        "capital":"Ottawa",
        "poblacion":"9000000",
        "idioma":["ingles,frances"],
        "status":True
        }

alumno1={"nombre":"Daniel",
         "apellido1":"Hernández",
         "apellido2":"Goonzales",
         "especialidad":"TI",
         "maricula":"123456",
         "area":"Software Multiplataforma",
         "modalidad":"Bilingüe",
         "maricula":"123456",
         "semestre":"2",
        }

#mostrar el contenido del dict
print(alumno1)

for i in alumno1:
    print(f"{i}={alumno1[i]}")


#Agregar un campo o atributo
alumno1["telefono"]="6181234567"
print(alumno1)

for i in alumno1:
    print(f"{i} = {alumno1[i]}")