eleccion = int(input("Presiona el numero donde deseas entrar:\n 1.Capacidad de copiar documentos dentro diresctorios\n 2.Capacidad de mover documentos dentro de directorios\n 3.Apliclacion de listas\n 4.Aplicacion de tuplas\n 5.Comparaciion de consumo de recuros y rendimiento\n "))
separador = ("×" * 25)
print(separador +"\n")

if eleccion == 3:
    import random
    separador = ("×" * 25)
    loop = 1
    dado= [1,2,3,4,5,6,7,8,9,10,11,12]
    print(separador +"\n")
    respuestas_validas=["si","SI","Si","sI"]
    while loop == 1:
        print(f"Estas son los lados del dado: ")
        print(*dado)
        jugadores= int(input("Dime cuantos jugadores van a tirar el dado "))
        print("Se procede a lanzar el dado creado")
        for turno in range(jugadores):
            print(f"Este es el resulado: {random.choice(dado)}")
            print(separador +"\n")
        continuar = str(input("Si desean tirar el dado de nuevo escribe\n Si\n No\n"))
        print(separador +"\n")
        if continuar in respuestas_validas :
            print("Nice")
            print(separador +"\n")
        else:
            print("Vuelve pronto crack")
            loop = 2
            print(separador +"\n")

if eleccion == 4:
    import random
    print(separador +"\n")
    loop = 1
    dadoT= (1,2,3,4,5,6,7,8,9,10,11,12)
    print(separador +"\n")
    respuestas_validas=("si","SI","Si","sI")
    while loop == 1:
        print(f"Estas son los lados del dado: ")
        print(*dadoT)
        jugadores= int(input("Dime cuantos jugadores van a tirar el dado "))
        print("Se procede a lanzar el dado creado")
        for turno in range(jugadores):
            print(f"Este es el resulado: {random.choice(dadoT)}")
            print(separador +"\n")
        continuar = str(input("Si desean tirar el dado de nuevo escribe\n Si\n No\n"))
        print(separador +"\n")
        if continuar in respuestas_validas :
            print("Nice")
            print(separador +"\n")
        else:
            print("Vuelve pronto crack")
            loop = 2
            print(separador +"\n")








