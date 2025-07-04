import agenda 
def main():
    agenda_contactos={}
    opcion=True

    while opcion:
        agenda.borrarPantalla()
        opcion=agenda.menuPrincipal()

        match opcion:
            case "1":
                agenda.agregar_contacto(agenda_contactos)
                agenda.esperarTecla()
            case "2":
                agenda.mostrar_contacto(agenda_contactos)
                agenda.esperarTecla()
            case "3":
                agenda.buscar_contacto(agenda_contactos)
                agenda.esperarTecla()
            case "4":
                agenda.modificar_contacto(agenda_contactos)
                agenda.esperarTecla()
            case "5":
                agenda.eliminar_contacto(agenda_contactos)
                agenda.esperarTecla()
            case "6":
                opcion=False
                agenda.borrarPantalla()
                print("\n\t Terminaste la ejecusion del sw")
            case _:
                input("\n\t Opcion invalida vuelva a intentar...")
                

if __name__ == "__main__":
    main()