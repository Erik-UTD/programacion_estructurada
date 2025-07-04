from paquete1 import modulos

print(modulos.saludar("Erik Gabriel Bueno Cao Romero"))

modulos.borrarPantalla()
nom,tel=modulos.solicitarDatos2()
print(f"\n\t.::Agenda Telefónica::.\n\t\tNombre:{nom}\n\t\tTelefono:{tel}")
modulos.espereTecla()