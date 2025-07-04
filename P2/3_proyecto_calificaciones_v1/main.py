"""
proyecto 3
Crear un proyecto que permita gestionar (administrar) calificaciones, colocar un menu de opciones para agregar, mostrar, calcular promedio calificaciones de un estudiante
Notas:
1.- Utilizar funciones y mandar llamar desde otro archivo(módulos)
2.- Utilizar list(bidimensional)  para almacenar el nombre del alumno, asi como sus 3 calificaciones
"""
import calificaciones

def main():
    datos = []

    opcion=True
    while opcion:
        calificaciones.borrarPantalla()
        opcion=calificaciones.menu_principal()

        match opcion:
            case "1":
                calificaciones.agregar_calificaciones(datos)
                calificaciones.esperarTecla()
            case "2":
                calificaciones.mostrar_calificaciones(datos)
                calificaciones.esperarTecla()
            case "3":
                calificaciones.calcular_promedios(datos)
                calificaciones.esperarTecla()
            case "4":
                calificaciones.modificar(datos)
                calificaciones.esperarTecla()
            case "5":
                calificaciones.borrarPantalla()
                print("\n\t Terminaste la ejecucion del sw")
            case _:
                input("\n\t.::Opcion invalida vuelve a intentarlo...")   
                

if __name__=="__main__":
    main()