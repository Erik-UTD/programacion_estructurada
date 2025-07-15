movies=[]

#dict para almacenar los atributos (nombre, categoria, clasificacion, genero, idioma)
pelicula={
            "nombre":"",
            "categoria":"",
            "clasificacion":"",
            "genero":"",
            "idioma":""

          }
         

import mysql.connector
from mysql.connector import Error


         

pelicula={} 

def borrar_pantalla():
    import os 
    os.system("cls")

def esperar_tecla():
    input("\n\tPresione cualquier tecla para continuar...")    


def conectar():
    try:
        conexion=mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="",
            database="bd_peliculas"
        )

        return conexion
    except Error as e:
        print(f"El error que sucedio es: {e}")
        return None




def crearPeliculas():
    borrar_pantalla()
    conexionBD=conectar()
    if conexionBD!=None:
        print("\n\t.::\U0001F4DD Alta de Peliculas::.\n")
        pelicula.update({"nombre":input("\U0001F4DD Ingresa el nombre: ").upper().strip()})
        pelicula.update({"categoria":input("\U0001F4DD Ingresa el categoria: ").upper().strip()})
        pelicula.update({"clasificacion":input("\U0001F4DD Ingresa el clasificacion: ").upper().strip()})
        pelicula.update({"genero":input("\U0001F4DD Ingresa el genero: ").upper().strip()})
        pelicula.update({"idioma":input("\U0001F4DD Ingresa el idioma: ").upper().strip()})

        ##AGREGAR REISTRO A LA BASE DE DATOS
        try:
            cursor=conexionBD.cursor()
            sql="INSERT INTO peliculas (nombre, categoria, clasificacion, genero, idioma) VALUES (%s, %s, %s, %s, %s)"
            val=(pelicula['nombre'],pelicula['categoria'],pelicula['clasificacion'],pelicula['genero'],pelicula['idioma'])
            #cursor.execute(
                #"INSERT INTO peliculas (id, nombre, categoria, clasificacion, genero, idioma) VALUES (NULL, %s, %s, %s, %s, %s)",(pelicula["nombre"],pelicula["categoria"],pelicula["clasificacion"],pelicula["genero"],pelicula["idioma"])
            #)
            cursor.execute(sql,val)
            conexionBD.commit()
            input("\n\t\t:::\u2705 ¡LA OPERACION SE REALIZO CON ÉXITO! :::")
        except Error as e:
            print("Error al intentar un registro en la base de datos")    


def mostrarPeliculas():
    borrar_pantalla()
    conexionBD=conectar()
    if conexionBD!=None:
        print("\n\t.::\U0001F50D Mostrar la Pelicula::.\n")
        cursor=conexionBD.cursor()
        sql="SELECT * FROM peliculas"
        cursor.execute(sql)
        registros=cursor.fetchall()
        if registros:
            print("\n\t mostrar peliculas")
            print(f"{'ID':<10}{'Nombre':<15}{'Categoria':<15}{'Clasificacion':<15}{'Genero':<15}{'Idioma':<15}")
            print(f"-"*80)
            for fila in registros:
                print(f"{fila[0]:<10}{fila[1]:<15}{fila[2]:<15}{fila[3]:<15}{fila[4]:<15}{fila[5]:<15}")
            print(f"-"*80)
        else:
            print("\t .::\u26A0 No hay peliculas en el sistema")



def buscarPeliculas():
    borrar_pantalla()
    conexionBD=conectar()
    if conexionBD!=None:
        print("\n\t.::\U0001F50D Mostrar la Pelicula::.\n")
        cursor=conexionBD.cursor()
        nombre=input("dame el nombre de la pelicula a buscar: ").upper().strip()
        sql="select * from peliculas where nombre=%s"
        val=(nombre,)
        cursor.execute(sql,val)
        registros=cursor.fetchall()
        if registros:
            print("\n\t mostrar peliculas")
            print(f"{'ID':<10}{'Nombre':<15}{'Categoria':<15}{'Clasificacion':<15}{'Genero':<15}{'Idioma':<15}")
            print(f"-"*80)
            for fila in registros:
                print(f"{fila[0]:<10}{fila[1]:<15}{fila[2]:<15}{fila[3]:<15}{fila[4]:<15}{fila[5]:<15}")
            print(f"-"*80)
        else:
            print("\t .::\u26A0 Esta pelicula no se encuentra...")




def borrarPeliculas():
    borrar_pantalla()
    conexionBD=conectar()
    if conexionBD!=None:
        print("\n\t.::\U0001F50D borrar Peliculas::.\n")
        cursor=conexionBD.cursor()
        nombre=input("dame el nombre de la pelicula a borrar: ").upper().strip()
        sql="select * from peliculas where nombre=%s"
        val=(nombre,)
        cursor.execute(sql,val)
        registros=cursor.fetchall()#el fetchall cuenta como uso de listas para el proyecto
        if registros:
            resp=input(f"Deseas borrar la pelicula de {nombre}? (Si/No): ").lower().strip()
            if resp=="si":
                sql="delete from peliculas where nombre=%s"
                val=(nombre,)
                cursor.execute(sql,val)
                conexionBD.commit()
                input("\n\t\t:::\u2705 ¡LA OPERACION SE REALIZO CON ÉXITO! :::")
        else:
            print("\t .::\u26A0 Esta pelicula no se encuentra...")






def modificarPeliculas():
    borrar_pantalla()
    conexionBD=conectar()
    if conexionBD!=None:
        print("\n\t.::\U0001F50D Modificar Peliculas::.\n")
        cursor=conexionBD.cursor()
        nombre=input("dame el nombre de la pelicula a modificar: ").upper().strip()
        sql="select * from peliculas where nombre=%s"
        val=(nombre,)
        cursor.execute(sql,val)
        registros=cursor.fetchall()
        if registros:
            print(f"{'ID':<10}{'Nombre':<15}{'Categoria':<15}{'Clasificacion':<15}{'Genero':<15}{'Idioma':<15}")
            print(f"-"*80)
            for fila in registros:
                print(f"{fila[0]:<10}{fila[1]:<15}{fila[2]:<15}{fila[3]:<15}{fila[4]:<15}{fila[5]:<15}")
            print(f"-"*80)
            resp=input(f"Deseas modficar la pelicula {nombre}? (Si/No): ").lower().strip()  
            if resp=="si":
                pelicula["nombre"]=input("\U0001F4DD Ingresa el nombre: ").upper().strip()
                pelicula["categoria"]=input("\U0001F4DD Ingresa el categoria: ").upper().strip()
                pelicula["clasificacion"]=input("\U0001F4DD Ingresa el clasificacion: ").upper().strip()
                pelicula["genero"]=input("\U0001F4DD Ingresa el genero: ").upper().strip()
                pelicula["idioma"]=input("\U0001F4DD Ingresa el idioma: ").upper().strip()

                sql="update peliculas set nombre=%s, categoria=%s, clasificacion=%s, genero=%s, idioma=%s where id=%s"
                val=(pelicula["nombre"],pelicula["categoria"],pelicula["calisificacion"],pelicula["genero"],pelicula["idioma"],nombre)
                cursor.execute(sql,val)
                conexionBD.commit()
                input("\n\t\t:::\u2705 ¡LA OPERACION SE REALIZO CON ÉXITO! :::")
        else:
            print("\t .::\u26A0 Esta pelicula no se encuentra...")
                
               
               

def borrarCaracteristica():
    #AGREGAR EXCEPCION
    borrar_pantalla()
    print("\n\t.::\U0001F4DB Borrar características a peliculas::.\n")
    if len(pelicula)>0:
        print("\n\t.::\U0001F4C2 Valores actuales::.")
        for i in pelicula:
            print(f"{(i)} : {pelicula[i]}")
        resp=input("\n\t Deseas borrar una característica? (\u2705 Si/\u274C No)  ").lower().strip()
        if resp=="si": 
            try:
                atributo=input("\n\t\U0001F4DDIngresa la caracteristica que deseas borrar: ").lower().strip()
                pelicula.pop(atributo)
                print("\n\t\t:::\u2705 ¡LA OPERACION SE REALIZO CON ÉXITO! :::")
                esperar_tecla()
                borrar_pantalla()
            except KeyError:
                print("\n\t.::\u26A0 Debes ingresar un un nombre que no tenga numeros...Intentalo de nuevo::..")    
    else:
        print("\t..::\u274CNo hay peliculas en el sistema")    






    """
    borrar_pantalla()
    print("\n\t.::Borrar características a peliculas::.\n")
    borr=input("Teclea la característica que deseas borrar").lower().strip()
    if not (borr) in pelicula:
        print("La pelicula que se tecleo no la tenemos.")
    else: 
        validar="si" 
        while borr in pelicula and validar=="si":
            validar=input("Deseas quitar o borrar la característica?").lower().strip()  
            if validar=="si":
                pelicula.pop(borr)
            else:
                print("Operacion cancelada con exito") 
                """   
                

        



"""
#def consultar():
    borrar_pantalla()
    print("\n\t.:: Consultar ó Mostrar las Peliculas ::.")
    if len(movies)>0:
        for i in range(0,len(movies)):
            print(f"{i+1}:{movies[i]}")
    else:
        print("\t..:: No hay peliculas en el sistema ::.")        
       


#def vaciar_peliculas():
    borrar_pantalla()
    print("\n\t.:: Borrar o quitar todas las peliculas ::.")
    resp=input("¿Deseas quitar o borrar todas las peliculas del sistema? (si)/(no)").lower()
    if resp=="si":
        movies.clear()
        input("\n\t\t::: ¡LA OPERACION SE REALIZO CON ÉXITO! :::")
    
#def buscar_peliculas():
    borrar_pantalla()
    print("\n\t.:: Buscar peliculas ::.")
    pelicula_buscar=input("Ingrese el nombre de la película a buscar: ").upper().strip()
    encontro=0
    if not(pelicula_buscar in movies):
        print("\n\t\t ¡No se encuentra la pelicula a buscar!")
    else:
        for i in range(0,len(movies)):
            if pelicula_buscar==movies[i]:
                print(f"La pelicula {pelicula_buscar} si la tenemos y esta en la casilla: {i+1}")
                encontro+=1
        if encontro>0:
            print(f"Tenemos {encontro} pelicula(s) con este titulo")
            input("\n\t\t::: ¡LA OPERACION SE REALIZO CON ÉXITO! :::")            






#def eliminar():
    borrar_pantalla()
    contador=0
    delete=input("Teclea la pelicula de la lista deseas eliminar: ").upper().strip()
    if not (delete) in movies:
        print("La pelicula que se tecleo no la tenemos.")
    else:
        while delete in movies and validar=="si":
            validar=input("Deseas quitar o borrar la pelicula del sistema (Si/No)").lower().strip()
            if validar=="si":
                pocision=movies.index(delete)
                print(f"La pelicula que se borro es {delete} y se encuentra en la casilla {pocision}")
                movies.remove(delete)
                contador+=1
                input("La operacion se realizo con exito")
        print(f"Se borro {contador} pelicula(s) con este titulo")        



#def actualizar_peliculas():
    borrar_pantalla()
    contador=0
    seleccion=input("teclee la pelicula que desea modificar: ").upper().strip()
    
    if not(seleccion) in movies:
        print("no se encontro la pelicula")
    else:
        for i in range(0,len(movies)):
            if seleccion==movies[i]:
                contador+=1

        if contador>1:
            print(movies)
            casilla=int(input(f"Se encontraron {contador} peliculas con el mismo nombre, ingresa la pocision de la pelicula"))
            cambio=input("Ingresa el reemplazo o cambio: ").upper().strip()
            casilla=casilla-1
            movies[casilla]=cambio
            print("El cambio se ha realizado correctamente")
            print(movies)
        else:
            cambio=input("Ingresa el reemplazo o cambio: ").upper().strip()
            movies[i]=cambio


"""





            
                

    
    
