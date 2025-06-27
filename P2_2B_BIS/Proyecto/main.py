"""
 Sistema informatico en consola para administración de un puesto de carne seca

"""
import carne 

def main():
    ventas=[]

    opcion=True

    while opcion:
        carne.borrarPantalla()
        opcion=carne.menuPrincipal()

        match opcion:
            case "1":
                carne.agregar(ventas)
                carne.esperar_tecla()
            case "2":
                carne.eliminar(ventas)
                carne.esperar_tecla()
            case "3":
                carne.actualizar_peliculas(ventas)
                carne.esperar_tecla()
            case "4":
                carne.mostrar(ventas)
                carne.esperar_tecla()
            case "5":
                carne.buscar(ventas)
                carne.esperar_tecla()
            case "6":
                opcion=False
                carne.borrar_pantalla()
                print("\n\t Terminaste la ejecusion del sw")
            case _:
                input("\n\t Opcion invalida vuelva a intentar...")

                

if __name__ == "__main__":
    main()



