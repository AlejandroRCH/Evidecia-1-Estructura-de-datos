#se empieza con la escritura del codigo del punto

#4.1 Aplicacion de listas como estructuras de datos nativas caso teorico

#En este caso haremos el codigo que simule el lanzamiento de un dado con 6 lados
import random
separador = ("×" * 25)
loop = 1
dado= [1,2,3,4,5,6]
print(separador)

while loop == 1:

    print(f"Estas son los lados del dado: ")
    print(*dado)
    jugadores= int(input("Dime cuantos jugadores van a tirar el dado "))
    print("Se procede a lanzar el dado creado")
    for turno in range(jugadores):
        print(f"Este es el resulado: {random.choice(dado)}")

    continuar = str(input("Si desean tirar el dado de nuevo escribe\n Si\n No\n"))
    
    if continuar == "si" or "Si" or "SI":
        print("Nice")
        print(separador)

    else:
        print("Vuelve pronto crack")
        loop = 2
        print(separador)







