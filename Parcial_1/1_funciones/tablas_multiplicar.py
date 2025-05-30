"""
Crear un programa que calcule e imprima cualquier tabla de multiplicar del 2

requisitos:
con funcuiones que regrese valor y utilice parametros

"""
#Verison1
num=int(input("Ingresa un numero a multiplicar"))
multi=num*1
print(f"{num} X 1 = {multi}")
multi=num*2
print(f"{num} X 2 = {multi}")
multi=num*3
print(f"{num} X 3 = {multi}")
multi=num*4
print(f"{num} X 4 = {multi}")
multi=num*5
print(f"{num} X 5 = {multi}")
multi=num*6
print(f"{num} X 6 = {multi}")
multi=num*7
print(f"{num} X 7 = {multi}")
multi=num*8
print(f"{num} X 8 = {multi}")
multi=num*9
print(f"{num} X 9 = {multi}")
multi=num*10
print(f"{num} X 10 = {multi}")

#Version 2

num=int(input("Dame el numero de la tabla a calcular: "))
for i in range(1,11):
    mult=num*i
    print(f"{num} x {i} = {mult}")


num=int(input("Dame el numero de la tabla a calcular: "))
i=1
while i<=10:
    mult=num*i
    print(f"{num} x {i} = {mult}")
    i+=1


#version3
def tabla(num):
    numero_bueno=num
    respuesta=" "
    for i in range(1,11):
        mult=numero_bueno*i
        respuesta+= f"\t{numero_bueno} x {i} = {mult}\n"
    return respuesta
    
numero1=int(input("Ingresa el numero a multiplicar: "))
resultado=tabla(numero1)
print(f"{resultado}")


