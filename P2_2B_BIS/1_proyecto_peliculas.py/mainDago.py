"""
Crear un proyecto que permita gestionar (administrar) peliculas, colocar un menu de opciones para agregar, eliminar, modificar y consultar peliculas.
Notas:
1.- Utilizar funciones y mandar llamar desde otro archivo
2.- Utilizar listas para almacenar los nombres de peliculas
"""
import peliculasDago
opcion=True
while opcion:
    peliculasDago.borrar_pantalla()
    print("\n\t\t\t..::CINPOLIS CLON::..\n\t\t..:::Sistema de Gestión De Películas :::....\n\t\t 1.-Agregar\n\t\t 2.-Eliminar\n\t\t 3.-Actualizar\n\t\t 4.-Consultar\n\t\t 5.-Buscar\n\t\t 6.-Vaciar\n\t\t 4.-SALIR")
    pregunta=input("\tSeleccione una opcion: ")

    match pregunta:
        case "1":
            peliculasDago.agregar()
            peliculasDago.esperar_tecla()
        case "2":
            peliculasDago.eliminar()
            peliculasDago.esperar_tecla()
        case "3":
            peliculasDago.actualizar_peliculas()
            peliculasDago.esperar_tecla()
        case "4":
            peliculasDago.consultar()
            peliculasDago.esperar_tecla()
        case "5":
            peliculasDago.buscar_peliculas()
            peliculasDago.esperar_tecla()

        case "6":
            peliculasDago.vaciar_peliculas()
            peliculasDago.esperar_tecla()

        case "7":
            opcion=False
            peliculasDago.borrar_pantalla()
            print("\n\t Terminaste la ejecusion del sw")
        case _:
            input("\n\t Opcion invalida vuelva a intentar...")