def borrarPantalla():
    import os
    os.system("cls")

def esperarTecla():
    input("\n\t\t\U0001F4DD Oprima cualquier tecla para continuar...")


def menuPrincipal():
    print("\n\t\t.:::\U0001F464  Sistema de Gestión de Agenda de Contactos \U0001F464  :::..\n\n\t\t 1.-\U0001F4DD Agregar contacto\n\t\t 2.-\U0001F4C2 Mostrar todos los contactos\n\t\t 3.-\U0001F50D Buscar contacto por nombre \n\t\t 4.-\U0001F50D Modificar contacto \n\t\t 5.-\U0001F50D Eliminar contacto\n\t\t \n\t\t 6.-\U0001F6AA SALIR" )
    opcion=input("\n\t\t\u2705 Elige  una opcion (1-6): ")
    return opcion

def agregar_contacto(agenda):
    borrarPantalla()
    print("\n\t\t.::Agregar contactos::. ")
    nombre=input("\t\tNombre del contacto: ").upper().strip()
    if nombre in agenda:
        print("\n\t\tEl contácto ya existe... ")
    else:
        tel=input("\t\tTelefono: ").strip()
        email=input("\t\tE-mail: ").lower().strip()
        #Agrehar el atributo "NOMBRE" al diccionario con los valores de tel y email en una lista
        agenda[nombre]=[tel,email]
        print("\n\t\t .::Accion realizada con éxito ::.")


def mostrar_contacto(agenda):
    borrarPantalla()
    print("\n\t\t.::Mostrar contactos::. ")
    if not agenda:
        print("\n\t\tNo existen contactos en la agenda")
    else:
       # for i in agenda:
            #print(f"{i}{agenda[i]}")
        for nombre,datos in agenda.items():
            print(f"\n\t\t{'Nombre: '+nombre}\n\t\t{'Teléfono: '+datos[0]}\n\t\t{'E-mail: '+datos[1]}")            


def buscar_contacto(agenda):
    borrarPantalla()
    print("\n\t\t.::Buscar contactos::. ")
    if not agenda:
        print("\n\t\tNo existen contactos en la agenda")
    else:
        encontro=False
        buscar=input("\t\tNombre del contacto: ").upper().strip()
        for i in agenda:
            if i == buscar:
                print(f"{i}{agenda[i]}")
                encontro=True
                print("\n\t\tOperacion exitosa")

        if not encontro:
            print("\n\t\tNo se encontro a nadie con ese nombre...")


def modificar_contacto(agenda):
    borrarPantalla()
    print("\n\t\t.::Modificar contactos::. ")
    if not agenda:
        print("\n\t\tNo existen contactos en la agenda")
    else:
        encontro=False
        buscar=input("\t\tNombre del contacto a modificar: ").upper().strip()
        for i in agenda:
            if i == buscar:
                print(f"{i}{agenda[i]}")
                dato=input("\t\tSelecciona el valor a modificar: 1.-Telefono 2.-E-mail ").lower().strip()
                if dato=="1":
                    telefono_nuevo=input("Nuevo numero de telefono: ").strip()
                    agenda[i][0]=telefono_nuevo
                    encontro=True
                    print("Operacion exitosa")
                elif dato=="2":
                    email=input("Nuevo E-mail: ").lower().strip()
                    agenda[i][1]=email
                    encontro=True
                    print("Cambio exitoso ")

        if not encontro:
            print("No se encontro a nadie con ese nombre...")


def eliminar_contacto(agenda):
    borrarPantalla()
    print("\n\t\t.::Borrar contactos::. ")
    if not agenda:
        print("No existen contactos en la agenda")
    else:
        encontro=False
        buscar=input("Nombre del contacto: ").upper().strip()
        for i in agenda:
            if i == buscar:
                print(f"{i}{agenda[i]}")
                encontro=True      
                confirmar=input("Seguro que quieres eliminar este usuario? ").lower().strip()

        if confirmar=="si":
            del agenda[buscar]
            encontro=True
            print("Operacion exitosa")
        else:
            print("Operacion cancelada correctamente...")                    

        if not encontro:
            print("No se encontro a nadie con ese nombre...")



