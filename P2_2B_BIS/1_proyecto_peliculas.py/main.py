"""
Crear un proyecto que permita gestionar (administrar) peliculas, colocar un menu de opciones para agregar, eliminar, modificar y consultar peliculas.
Notas:
1.- Utilizar funciones y mandar llamar desde otro archivo
2.- Utilizar listas para almacenar los nombres de peliculas
"""
import os
import peliculas
movies=["transformers","zootopia","hola"]
opcion=True
while opcion:
    peliculas.borrar_pantalla()
    print("\t.::Menu de opciones::. \n\t 1.-Agregar\n\t 2.-Eliminar\n\t 3.-Actualizar\n\t 4.-Consultar\n\t 5.-Buscar\n\t 6.-Vaciar\n\t 4.-SALIR")
    pregunta=input("Seleccione una opcion: ")

    match pregunta:
        case "1":
            peliculas.borrar_pantalla()
            print("Has seleccionado agregar")
            peliculas.insertar()
            peliculas.esperar_tecla()
        case "2":
            peliculas.borrar_pantalla()
            print("has seleccionado eliminar")
            peliculas.eliminar()
            peliculas.esperar_tecla()
        case "3":
            peliculas.borrar_pantalla()
            print("has seleccionado modificar")
            peliculas.esperar_tecla()
        case "4":
            peliculas.borrar_pantalla()
            print("has seleccionado consultar")
            peliculas.consultar()
            peliculas.esperar_tecla()
        case "5":
            print("x")

        case "6":
            print("x")

        case "7":
            print("Has seleccionado salir...")
            opcion=False
        case _:
            os.system("cls")
            input("Opcion invalida vuelva a intentar...")