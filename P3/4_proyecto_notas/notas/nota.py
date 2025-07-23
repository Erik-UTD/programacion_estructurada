from conexionBD import *
import datetime

def crear(usuario_id,titulo,descripcion):
    try:
        sql="insert into notas (usuario_id,titulo,descripcion,fecha) values (%s,%s,%s,NOW())"
        val=(usuario_id,titulo,descripcion)
        cursor.execute(sql,val)
        conexion.commit()

        return True
    except:
        return False
    
def checar_id(usuario_id, id):
    if id == usuario_id:
        print("EXITOOOOO")
        return True


def mostrar(usuario_id):
    try:
        sql="select * from notas where usuario_id=%s"
        val=(usuario_id,)
        cursor.execute(sql,val)
        return cursor.fetchall()
    
    except:
        return []    


def cambiar(id,titulo,descripcion):
    try:
        #Primero mostrar lo que hay
        cursor.execute("update notas set titulo=%s, descripcion=%s,fecha=NOW() where id=%s", (titulo,descripcion,id))
        conexion.commit()
        
        return True
    except:
        return False
    

def borrar(id):
    try:
        #codigo para asegurarse de que la nota existe (Mostrar las notas primero, eliminar con ID )
        cursor.execute("delete from notas where id=%s", (id,))
        conexion.commit()
        return True
    except:
        return False