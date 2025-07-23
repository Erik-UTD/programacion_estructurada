import mysql.connector
from mysql.connector import Error


def borrarPantalla():
    import os
    os.system("cls")

def esperarTecla():
    input("\n\t\t\U0001F4DD Oprima cualquier tecla para continuar...")

def conectar():
    try:
        conexion=mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="",
            database="bd_calificaciones"
        )

        return conexion
    except Error as e:
        print(f"El error que sucedio es: {e}")
        return None



def menu_principal():
    print("\n\t\t.:::\U0001F4C2 Sistema de Gestión De calificaciones \U0001F4C2 :::...\n\t\t 1.-\u2705 Agregar\n\t\t 2.-\U0001F4DB Mostrar\n\t\t 3.-\U0001F50D Calcular promedio\n\t\t 4.-\U0001F6AA Modificar \n\t\t 5.- SALIR" )
    opcion=input("\n\t\t\U0001F50D Seleccione una opcion (1-4): ")
    return opcion


def agregar_calificaciones(lista):
    borrarPantalla()
    conexionBD=conectar()
    if conexionBD!=None:
        print("\t\t\U0001F4DD Agregar Calificaciones \U0001F4DD")
        nombre=input("\n\t\t\U0001F464 Nombre del Alumno: ").upper().strip()
        calificaciones=[]
        for i in range(1,4):
            continua=True
            while continua:
                try:
                    cal=float(input(f"\t\t\U0001F4DD Calificacion {i}: "))
                    if cal>=0 and cal<11:
                        calificaciones.append(cal)
                        continua=False
                    else: 
                        print("\n\t\t\u26A0 Ingresa un numero valido")  
                except ValueError:
                    print("\n\t\t\U0001F4DDIngresa un valor numérico")                     
        lista.append([nombre]+calificaciones)
        print("\n\t\t\u2705 .::Accion realizada con exito::. \u2705")

        try:  
            cursor = conexionBD.cursor()
            sql = "insert into calificaciones (nombre,calificacion1,calificacion2,calificacion3) values (%s,%s,%s,%s)"
            values = (nombre, calificaciones[0], calificaciones[1], calificaciones[2])
            cursor.execute(sql, values)
            conexionBD.commit()
            print("\n\t\t :::\u2705 LA OPERACION SE REALIZO CON EXITO! \u2705:::")
        except Error as e:
            print("\n\t\t \u26A0 Error al intentar conectar a la base de datos \u26A0")




def mostrar_calificaciones(lista):
    borrarPantalla()
    conexionBD=conectar()
    print("\t\t\U0001F4C2 .::Mostrar Calificaciones::. \U0001F4C2")
    if conexionBD!=None:
        print("\n\t.::\U0001F50D Mostrar calificaciones::.\n")
        cursor=conexionBD.cursor()
        sql="SELECT * FROM calificaciones"
        cursor.execute(sql)
        registros=cursor.fetchall()
        if registros:
            print("\n\t mostrar calificaciones")
            print(f"{'ID':<10}{'Nombre':<15}{'Calificación 1':<15}{'Calificación 2':<15}{'Calificación 3':<15}")
            print(f"-"*80)
            for fila in registros:
                print(f"{fila[0]:<10}{fila[1]:<15}{fila[2]:<15}{fila[3]:<15}{fila[4]:<15}")
            print(f"-"*80)
        else:
            print("\t .::\u26A0 No hay peliculas en el sistema")


"""""
def calcular_promedios(lista):
    borrarPantalla()
    print("Calcular promedio de calificaciones ")
    if len(lista)>0:
        print(f"{'Alumno':<15}{'Promedio':<10}")
        print(f"{'-'*30}")
        promedio_grupal=0
        for fila in lista:
            nombre=fila[0]
            i=0
            suma=0
            promedio=0
            while i<=3:
                suma+=fila[i]
                i+=1
            promedio=suma/3
            print(f"{nombre:<15}{promedio:.2f}")  
            promedio_grupal+=promedio  
        print(f"{'-'*30}")
        promedio_grupal=promedio_grupal/len(lista)
        print(f"El promedio grupal es: {promedio_grupal}")

    else:
        print("La lista no contiene elementos") 

"""

def calcular_promedios(lista):
    borrarPantalla()
    print("\t\t\U0001F4DD..:Calcular promedio de calificaciones:..\U0001F4DD ")
    if len(lista)>0:
        print(f"\n\t\t{'Alumno':<15}{'Promedio':<10}")
        print(f"\t\t{'-'*30}")
        promedio_grupal=0
        for fila in lista:
            nombre=fila[0]
            promedio=sum(fila[1:])/3
            print(f"\t\t{nombre:<15}{promedio:.2f}")  
            promedio_grupal+=promedio  
        print(f"\t\t{'-'*30}")
        promedio_grupal=promedio_grupal/len(lista)
        print(f"\n\t\t\U0001F389 El promedio grupal es: {promedio_grupal} ")

    else:
        print("\n\t\t\u26A0 La lista no contiene elementos...") 
     

def modificar(lista):
    borrarPantalla()
    conexionBD=conectar()
    print("\t\t\U0001F4DD..:Modificar datos:..\U0001F4DD ")
    cursor=conexionBD.cursor()
    sql="SELECT * FROM calificaciones"
    cursor.execute(sql)
    registros=cursor.fetchall()
    if registros:
        print(f"{'ID':<10}{'Nombre':<15}{'Calificacion 1':<15}{'Calificacion 2':<15}{'Califiacion 3':<15}")
        print(f"-"*60)
        for fila in registros:
            print(f"{fila[0]:<10}{fila[1]:<15}{fila[2]:<15}{fila[3]:<15}{fila[4]:<15}")
        print(f"-"*60)

    print("\n\t\t.::Modificar Califiaciones::. ")
    if conexionBD!=None:
        id=input("\t\tID del contacto a modificar: ").upper().strip()
        sql="select * from calificaciones where id=%s"
        val=(id,)
        cursor.execute(sql,val)
        registros=cursor.fetchall()
        if registros:
            resp=input(f"Deseas modficar la pelicula {id}? (Si/No): ").lower().strip()
            if resp=="si":
                borrarPantalla()
                nombre_nuevo=input("Nuevo nombre: ").upper().strip()
                cal_1=input("Calificacion 1: ").strip()
                cal_2=input("Calificacion 2:  ").lower().strip()
                cal_3=input("Calificacion 3:  ").lower().strip()
                sql="update calificaciones set nombre=%s, calificacion1=%s, calificacion2=%s, calificacion3=%s where id=%s"
                val=(nombre_nuevo, cal_1, cal_2, cal_3, id)
                cursor.execute(sql,val)
                conexionBD.commit()
                input("\n\t\t:::\u2705 ¡LA OPERACION SE REALIZO CON ÉXITO! :::")
        else:
            print("No existe nadie con ese ID, vuelva a intentar...")
   



        

                

        
            




#MODIFICAR SIN BASE DE DATOS (DENTRO DE LA LISTA
"""
def modificar(lista):
    borrarPantalla()
    print("\t\t\U0001F4DD..:Modificar datos:..\U0001F4DD ")
    if len(lista)>0:
        print(f"\n\t\t{'Nombre':<15}{'Cal.1':<10}{'Cal.2':<10}{'Cal.3':<10}")
        print(f"\t\t{'-'*40}")
        siguiente=True
        while siguiente:
            for fila in lista:
                print(f"\t\t{fila[0]:<15}{fila[1]:<10}{fila[2]:<10}{fila[3]:<10} ")
                respuesta=input("deseas modificar el nombre o alguna calificacion?").lower().strip()
                if respuesta=="si":
                    try:
                        opcion=input("Selecciona el numero de lo que deseas modificar: 1.-nombre \n2.- calificacion 1 \n3.- calificacion 2 \n4.- calificacion 3")
                        match opcion:
                            case "1":
                                n_nuevo=input("Ingresa el nombre nuevo: ")
                                fila[0]=n_nuevo
                                print("Operacion realizada con exito")
                                siguiente=False
                            case "2":
                                c1_nuevo=float(input("Ingresa la calificacion nueva: "))
                                fila[1]=c1_nuevo
                                print("Operacion realizada con exito")
                                siguiente=False
                            case "3":
                                c2_nuevo=float(input("Ingresa la calificacion nueva: "))
                                fila[2]=c2_nuevo
                                print("Operacion realizada con exito")
                                siguiente=False
                            case "4":
                                c3_nuevo=float(input("Ingresa la calificacion nueva: "))
                                fila[3]=c3_nuevo
                                print("Operacion realizada con exito")
                                siguiente=False
                    except ValueError:
                        print("Debes ingresar un numero...Vuelve a intentarlo")        
                else:
                    print("\n\t\t\u26A0 No hay calificaciones registradas")
"""