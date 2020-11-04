#se empieza con la escritura del codigo del punto

#4.1 Aplicacion de listas como estructuras de datos nativas caso teorico

#En este caso haremos el codigo que simule el lanzamiento de un dado con 6 lados

separador = ("×" * 25)
loop = True
dado= list
lados_dado= int(input("Dame el numero de caras que quieras para hacer el dado: \n"))
for x in range(caras):
    dado.append(x + 1)
print(f"Estas son los lados del dado:"{dado})
print(separador)

jugadores= int(input("Dime cuantos jugadores van a tirar el dado"))


while loop == True:
    print("Se procede a lanzar el dado creado")
    for turno in range(jugadores):
        print(f"Este es el resulado: {random.choice(dado)}")

    continuar = input("Si desean tirar el dado de nuevo escribe\n Si\n No")
    if continuar == "si" or "Si" or "SI":
        print("Nice")
    else:
        print("Vuelve pronto crack")
        loop = False  





