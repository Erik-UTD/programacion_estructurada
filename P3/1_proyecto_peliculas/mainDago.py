"""
Crear un proyecto que permita gestionar (administrar) peliculas, colocar un menu de opciones para agregar, eliminar, modificar y consultar peliculas.
Notas:
1.- Utilizar funciones y mandar llamar desde otro archivo
2.- Utilizar dict  para almacenar los siguientes atributos: (nombre, categoria, clasificacion, genero, idioma)
3.- Utilizar e implementar una base de datos para gestionar las peliculas
"""
import peliculasDago
opcion=True
while opcion:
    peliculasDago.borrar_pantalla()
    print("\n\t\t\t..::\U0001F389 CINEPOLIS CLON::..\n\t\t..:::\U0001F4C2 Sistema de Gestión De Películas :::....\n\t\t 1.-\u2705 crear\n\t\t 2.-\U0001F4DB borrar\n\t\t 3.-\U0001F50D Mostrar\n\t\t 4.-\U0001F4DD Modificar \n\t\t 5.-\U0001F6AA Buscar \n\t\t 6.-\U0001F6AA SALIR")
    pregunta=input("\t\U0001F50D Seleccione una opcion: ")

    match pregunta:
        case "1":
            peliculasDago.crearPeliculas()
            peliculasDago.esperar_tecla()
        case "2":
            peliculasDago.borrarPeliculas()
            peliculasDago.esperar_tecla()
        case "3":
            peliculasDago.mostrarPeliculas()
            peliculasDago.esperar_tecla()
        case "4":
            peliculasDago.modificarPeliculas()
            peliculasDago.esperar_tecla()
        case "5":
            peliculasDago.buscarPeliculas()
            peliculasDago.esperar_tecla()
        case "6":
            opcion=False
            peliculasDago.borrar_pantalla()
            print("\n\t Terminaste la ejecusion del sw")
        case _:
            input("\n\t Opcion invalida vuelva a intentar...")