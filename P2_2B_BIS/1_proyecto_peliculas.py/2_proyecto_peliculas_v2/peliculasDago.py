movies=[]

#dict para almacenar los atributos (nombre, categoria, clasificacion, genero, idioma)
"""pelicula={
            "nombre":"",
            "categoria":"",
            "clasificacion":"",
            "genero":"",
            "idioma":""

          }
         """

pelicula={} 

def borrar_pantalla():
    import os 
    os.system("cls")

def esperar_tecla():
    input("\n\tPresione cualquier tecla para continuar...")    



def crearPeliculas():
    borrar_pantalla()
    print("\n\t.::\U0001F4DD Alta de Peliculas::.\n")
    pelicula.update({"nombre":input("\U0001F4DD Ingresa el nombre: ").upper().strip()})
    pelicula.update({"categoria":input("\U0001F4DD Ingresa el categoria: ").upper().strip()})
    pelicula.update({"clasificacion":input("\U0001F4DD Ingresa el clasificacion: ").upper().strip()})
    pelicula.update({"genero":input("\U0001F4DD Ingresa el genero: ").upper().strip()})
    pelicula.update({"idioma":input("\U0001F4DD Ingresa el idioma: ").upper().strip()})
    input("\n\t\t:::\u2705 ¡LA OPERACION SE REALIZO CON ÉXITO! :::")


def mostrarPeliculas():
    borrar_pantalla()
    print("\n\t.::\U0001F50D Mostrar la Pelicula::.\n")
    if len(pelicula)>0:
        for i in pelicula:
            print(f"\t {(i)} : {pelicula[i]}")
    else:
        print("\t .::\u26A0 No hay peliculas en el sistema")     


def borrarPeliculas():
    borrar_pantalla()
    print("\n\t.::\U0001F4DB Borrar o Quitar todas las peliculas ::.\n")
    resp=input("\u26A0 Deseas borrar o quitar todas las peliculas del sistema? (\u2705Si/\u274CNo)")
    if resp=="si":
        pelicula.clear()
        print("\n\t\t:::\u2705 ¡LA OPERACION SE REALIZO CON ÉXITO! :::")
    else:
        print("\t .::\u274C Operacion cancelada con exito")    


def agregarCaracteristicaPeliculas():
    borrar_pantalla()
    print("\n\t.::\U0001F501 Agregar características a peliculas::.\n")
    atributo=input("\U0001F4DD Ingresa la nueva característica de la pelicula").lower().strip()
    valor=input("\U0001F4DD Ingresa el valor de la nueva caracteristica de la pelicula").upper().strip()
    pelicula.update({atributo:valor})
    print("\n\t\t:::\u2705 ¡LA OPERACION SE REALIZO CON ÉXITO! :::")


def modificarPeliculas():
    borrar_pantalla()
    print("\n\t.::\U0001F4DD Modificar caracteristicas de peliculas ::.")
    if len(pelicula)>0:
        print(f"\n\t\U0001F50D Valores actuales: \n ")
        for i in pelicula:
            print(f"{(i)} : {pelicula[i]}")
            resp=input(f"\n\t\U0001F501 Deseas cambiar el valor de {i}? ")
            if resp=="si":
                pelicula.update({f"{i}":input("\tEl nuevo valor es: ").upper().strip()})
                print("\n\t\t:::\u2705 ¡LA OPERACION SE REALIZO CON ÉXITO! :::")
    else:
        print("\n\t..::\u274C No existen peliculas en sistema::..")
        esperar_tecla()
                
               
               

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





            
                

    
    
