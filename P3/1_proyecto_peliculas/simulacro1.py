lista=[]

if len(lista)==0:
    resp="si"
    while resp=="si":
        frase=input("Ingresa una frase o palabra").upper().strip()
        lista.append(frase)
        resp=input("Deseas repetir el proceso? (si/no) ").lower().strip()
        
    print(lista)    
