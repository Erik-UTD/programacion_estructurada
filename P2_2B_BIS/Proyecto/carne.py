"""
 Sistema informatico en consola para administración de un puesto de carne seca

"""
costo_carne=145.00

def borrarPantalla():
    import os
    os.system("cls")

def esperar_tecla():
    input("\n\t\t\U0001F4DD Oprima cualquier tecla para continuar...")


def menuPrincipal():
    print("\n\t\t.:::\U0001F4C2 Sistema de Gestión de ventas de La Vaquerita \U0001F4C2 :::..\n\t\t 1.-\u2705 Agregar\n\t\t 2.-\U0001F4DB Eliminar\n\t\t 3.-\U0001F50D Actualizar \n\t\t 4.-\U0001F6AA Mostrar \n\t\t 5.- Buscar \n\t\t 6.-Salir"  )
    opcion=input("\n\t\t\U0001F50D Seleccione una opcion (1-4): ")
    return opcion


def agregar(lista):
    borrarPantalla()
    print("\t\t\U0001F4DD Agregar ventas  \U0001F4DD")
    personas=[]
    continuar="si"
    while continuar=="si":
        nombre=input("Nombre del cliente: ").upper().strip()
        personas.append(nombre)
        comprado=int(input("Numero de carnes compradas: "))
        personas.append(comprado)
        monto=comprado*costo_carne
        print(f"Monto a pagar: {monto}")
        personas.append(monto)
        recibido=float(input("\nDinero recibido: "))
        personas.append(recibido)
        cambio=recibido-monto
        print(f"cambio a entregar: {cambio}")
        personas.append(cambio)
        lista.append(personas)
        print("\n\t\t\u2705 .::Accion realizada con exito::. \u2705")
        continuar=input("Deseas agregar otro cliente? (Si/No) ").lower().strip()


def mostrar(lista):
    borrarPantalla()
    print("\t\t\U0001F4C2 .::Mostrar ventas::. \U0001F4C2")
    if len(lista)>0:
        print(f"\n\t\t{'Nombre':<15}{'Comprado':<10}{'Monto':<10}{'Recibido':<10}{'cambio':<10}")
        print(f"\t\t{'-'*50}")
        for fila in lista:
            print(f"\t\t{fila[0]:<15}{fila[1]:<10}{fila[2]:<10}{fila[3]:<10}{fila[4]:<10} ")
    else:
        print("\n\t\t\u26A0 No hay calificaciones registradas")

    print(f"\t\t{'-'*50}")
    cuantos=len(lista)
    print(f"\n\t\t\U0001F4C2 Son {cuantos} alumnos")



        


