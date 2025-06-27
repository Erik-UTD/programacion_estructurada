movies=["transformers","zootopia","hola"]
def borrar_pantalla():
    import os 
    os.system("cls")

def esperar_tecla():
    input("Presione cualquier tecla para continuar...")    



def insertar():
    nombre=""
    resp=""
    opc=True
    while opc:
        nombre=input("Ingresa la pelicula que deseas agreagar: ")
        movies.append(nombre)
        resp=input("Deseas agregar otra pelicula? ").lower()
        if resp=="si":
            opc=True
        else:
            opc=False    
    print("los nombres se han agregado correctamente")
    print(movies)


def eliminar():
    print(movies)
    delete=input("Teclea la pelicula de la lista deseas eliminar?").lower() 
    match delete:
        case "transformers":
            movies.pop(0)
        case "zootopia":
            movies.pop(1)       
        case "hola":
            movies.pop(2)   
    print(movies)
    print("La pelicula se ha eliminado correctamente")


def modificar():
    print(movies)
    seleccion=input("teclee la pelicula que desea modificar: ")
    for i in movies:
        pelicula=i
        if pelicula==seleccion:
            modificacion=input("Ingresa la nueva pelicula o su respectivo cambio: ")
            
            


def consultar():
    opcion="si"
    while opcion=="si":
        pregunta=input("teclee la pelicula que desea consultar: ").lower()
        for i in movies:
            pelicula=i

        if pelicula == pregunta:
            print("La pelicula está disponible")
        else:
            print("La pelicula no esta disponble")

        opcion=input("Deseas intentar de nuevo?").lower()


                

    
    
