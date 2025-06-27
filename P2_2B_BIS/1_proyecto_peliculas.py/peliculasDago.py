movies=[]
def borrar_pantalla():
    import os 
    os.system("cls")

def esperar_tecla():
    input("Presione cualquier tecla para continuar...")    



def agregar():
    borrar_pantalla()
    print("\n\t.::Alta de Peliculas::.")
    movies.append(input("Ingresa el nombre: ").upper().strip())
    input("\n\t\t::: ¡LA OPERACION SE REALIZO CON ÉXITO! :::")


def consultar():
    borrar_pantalla()
    print("\n\t.:: Consultar ó Mostrar las Peliculas ::.")
    if len(movies)>0:
        for i in range(0,len(movies)):
            print(f"{i+1}:{movies[i]}")
    else:
        print("\t..:: No hay peliculas en el sistema ::.")        

def vaciar_peliculas():
    borrar_pantalla()
    print("\n\t.:: Borrar o quitar todas las peliculas ::.")
    resp=input("¿Deseas quitar o borrar todas las peliculas del sistema? (si)/(no)").lower()
    if resp=="si":
        movies.clear()
        input("\n\t\t::: ¡LA OPERACION SE REALIZO CON ÉXITO! :::")
    
def buscar_peliculas():
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






def eliminar():
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



def actualizar_peliculas():
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









            
                

    
    
