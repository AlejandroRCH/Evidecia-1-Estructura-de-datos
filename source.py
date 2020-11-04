#se empieza con la escritura del codigo del punto

#4.1 Aplicacion de listas como estructuras de datos nativas caso teorico

#En este caso necesitamos crear una playlist
#a continuacion se le pide al usuario que inserte una nueva cancion
separador= ( "×" * 25)
playlist= [" Fresco\n","Islas\n","Poli\n","Las Mañanitas\n","Es Épico\n","Dare\n"]
print("Esta es la playlist actual:")
print(*playlist)
print(separador)
#A continuacion se le dara al usuario la opcion de agregar algo mas a la lista
nueva_rola= list
nueva_rola = input("Dime la cancion que deseas agregar ")
playlist.append((nueva_rola)+"\n")
print(*playlist)
print(separador)

#A continuacion se le pide al usuario que agregue 3 canciones mas

for turno in range(3):
    nueva_rola= input("Agrega una nueva cancion ")
    playlist.append((nueva_rola)+"\n")

print(*playlist)
print(separador)

#A continuacion se le pide al usuario que elimine una cancion de la playlist

print(*playlist)
borrar = input("Dime el nombre de la cancion que quieres borrar: ")
playlist.remove(borrar)
print(*playlist)