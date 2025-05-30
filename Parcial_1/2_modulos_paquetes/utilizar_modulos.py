#Primer forma de utilizar los módulos
import modulos

modulos.borrarPantalla()

print(modulos.saludar("Erik Gabriel Bueno Cao Romero"))

#2da forma de utilizar modulos
from modulos import saludar,borrarPantalla

borrarPantalla()
print(saludar("zzzzzzzzzzzzzzzz"))


nombre=input("Ingresa el nombre de contacto: ")
telefono=input("Ingrese su numero de telefono: ")
nom,tel=modulos.solicitarDatos4(nombre, telefono)
print(f"\tNombre Completo: {nom}\n\tTelefono:{tel}")