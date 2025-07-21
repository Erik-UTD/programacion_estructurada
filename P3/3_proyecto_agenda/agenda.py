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
            database="bd_agenda"
        )

        return conexion
    except Error as e:
        print(f"El error que sucedio es: {e}")
        return None
    

def menuPrincipal():
    print("\n\t\t.:::\U0001F464  Sistema de Gestión de Agenda de Contactos \U0001F464  :::..\n\n\t\t 1.-\U0001F4DD Agregar contacto\n\t\t 2.-\U0001F4C2 Mostrar todos los contactos\n\t\t 3.-\U0001F50D Buscar contacto por nombre \n\t\t 4.-\U0001F50D Modificar contacto \n\t\t 5.-\U0001F50D Eliminar contacto\n\t\t \n\t\t 6.-\U0001F6AA SALIR" )
    opcion=input("\n\t\t\u2705 Elige  una opcion (1-6): ")
    return opcion

def agregar_contacto(agenda):
    borrarPantalla()
    conexionBD=conectar()
    cursor=conexionBD.cursor()

    print("\n\t\t.::Agregar contactos::. ")
    nombre=input("\t\tNombre del contacto: ").upper().strip()
    tel=input("\t\tTelefono: ").strip()
    email=input("\t\tE-mail: ").lower().strip()
    #Agrehar el atributo "NOMBRE" al diccionario con los valores de tel y email en una lista
    sql="insert into contactos (nombre, telefono, email) values (%s,%s,%s)"
    val=(nombre,tel,email)
    cursor.execute(sql,val)
    conexionBD.commit()
    print("\n\t\t .::Accion realizada con éxito ::.")   


def mostrar_contacto(agenda):
    borrarPantalla()
    print("\n\t\t.::Mostrar contactos::. ")
    conexionBD=conectar()
    cursor=conexionBD.cursor()
    if conexionBD!=None:
        print("\n\t.::\U0001F50D Mostrar contactos::.\n")
        sql="SELECT * FROM contactos"
        cursor.execute(sql)
        registros=cursor.fetchall()
        if registros:
            print("\n\t mostrar peliculas")
            print(f"{'ID':<10}{'Nombre':<15}{'telefono':<15}{'E-mail':<15}")
            print(f"-"*60)
            for fila in registros:
                print(f"{fila[0]:<10}{fila[1]:<15}{fila[2]:<15}{fila[3]:<15}")
            print(f"-"*60)
        else:
            print("\t .::\u26A0 No hay contactos en el sistema")
          


def buscar_contacto(agenda):
    borrarPantalla()
    print("\n\t\t.::Buscar contactos::. ")
    conexionBD=conectar()
    cursor=conexionBD.cursor()
    if conexionBD!=None:
        nombre=input("\t\tNombre del contacto a buscar: ").upper().strip()
        sql="select * from contactos where nombre=%s"
        val=(nombre,)
        cursor.execute(sql,val)
        registros=cursor.fetchall()
        if registros:
            print("\n\t mostrar contactos")
            print(f"{'ID':<10}{'Nombre':<15}{'telefono':<15}{'E-mail':<15}")
            print(f"-"*60)
            for fila in registros:
                print(f"{fila[0]:<10}{fila[1]:<15}{fila[2]:<15}{fila[3]:<15}")
            print(f"-"*60)
        else:
            print("\t .::\u26A0 No hay contactos en el sistema")



def modificar_contacto(agenda):
    borrarPantalla()
    conexionBD=conectar()
    cursor=conexionBD.cursor()
    sql="SELECT * FROM contactos"
    cursor.execute(sql)
    registros=cursor.fetchall()
    if registros:
        print(f"{'ID':<10}{'Nombre':<15}{'Telefono':<15}{'E-mail':<15}")
        print(f"-"*60)
        for fila in registros:
            print(f"{fila[0]:<10}{fila[1]:<15}{fila[2]:<15}{fila[3]:<15}")
        print(f"-"*60)

    print("\n\t\t.::Modificar contactos::. ")
    if conexionBD!=None:
        id=input("\t\tID del contacto a modificar: ").upper().strip()
        sql="select * from contactos where id=%s"
        val=(id,)
        cursor.execute(sql,val)
        registros=cursor.fetchall()
        if registros:
            resp=input(f"Deseas modficar la pelicula {id}? (Si/No): ").lower().strip()
            if resp=="si":
                nombre_nuevo=input("Nuevo nombre: ").upper().strip()
                telefono_nuevo=input("Nuevo numero de telefono: ").strip()
                email=input("Nuevo E-mail: ").lower().strip()
                sql="update contactos set nombre=%s, telefono=%s, email=%s where id=%s"
                val=(nombre_nuevo,telefono_nuevo,email,id)
                cursor.execute(sql,val)
                conexionBD.commit()
                input("\n\t\t:::\u2705 ¡LA OPERACION SE REALIZO CON ÉXITO! :::")
        else:
            print("No existe ese contacto...")


def eliminar_contacto(agenda):
    borrarPantalla()
    conexionBD=conectar()
    cursor=conexionBD.cursor()
    if conexionBD!=None:
        sql="SELECT * FROM contactos"
        cursor.execute(sql)
        registros=cursor.fetchall()
        if registros:
            print(f"{'ID':<10}{'Nombre':<15}{'Telefono':<15}{'E-mail':<15}")
            print(f"-"*60)
            for fila in registros:
                print(f"{fila[0]:<10}{fila[1]:<15}{fila[2]:<15}{fila[3]:<15}")
            print(f"-"*60)

        print("\n\t\t.::Borrar contactos::. ")

        id=input("ID del contacto a borrar: ").strip()
        sql="select * from contactos where id=%s"
        val=(id,)
        cursor.execute(sql,val)
        registros=cursor.fetchall()
        if registros:
            resp=input(f"Deseas borrar el contacto {id}? si/no").lower().strip()
            if resp=="si":
                sql="delete from contactos where id=%s"
                val=(id,)
                cursor.execute(sql,val)
                conexionBD.commit()
                input("\n\t\t:::\u2705 ¡LA OPERACION SE REALIZO CON ÉXITO! :::")
                
        else:
            print("ningun contacto tiene ese ID...vuelva a intentar")


