eleccion = int(input("Presiona el numero donde deseas entrar:\n 1.Capacidad de copiar documentos dentro diresctorios\n 2.Capacidad de mover documentos dentro de directorios\n 3.Apliclacion de listas\n 4.Aplicacion de tuplas\n 5.Comparaciion de consumo de recuros y rendimiento\n "))
separador = ("»" * 25)
print(separador +"\n")



if eleccion == 1:
    import os
    import shutil
    import time
    print(f"Directorio de trabajo ACTUAL:\n{os.getcwd()}\n")
    print("Carpetas y documentos existentes en este directorio:\n ")
    
    for raiz, dirs, archivos in os.walk(".", topdown=False):
        for nombre in archivos:
            print(os.path.join(raiz, nombre))
        for nombre in dirs:
            print(os.path.join(raiz, nombre))
    print(separador) # =================================================
    print(separador)
    print("****PRUEBA COPIAR UN ARCHIVO DE LOS QUE SE MUESTRAN EN LA BARRA DE LA IZQUIERDA****\n")
    print("NOTA 1: Puedes copiar y pegar los documentos desplegados en pantalla para evitar errores.\n")
    print("NOTA 2: Recuerda, si un documento tiene espacios en blanco, mayusculas, signos, etc. tambien cuentan\n")
    respuesta_copiar = "si"
    while respuesta_copiar == "si":
        copiar_doc = input("¿Que documento quieres copiar?: ")
        ruta_archivo = shutil.copy(copiar_doc, copiar_doc+" - copia")
        print(f"Este es el documento copia: {ruta_archivo}\n")
        respuesta_copiar = input("¿Quieres copiar algun otro archivo? 'si''no':")
        
        if respuesta_copiar == "no":
            print("Esta bien...Revisa que documentos creaste\n ")

if eleccion == 2:
    import os
    import shutil
    import time
    segundos = 5
    print("****PRUEBA MOVER UN ARCHIVO DE LOS QUE ACABAS DE COPIAR****\n")
    print("CONSEJO 1: la CARPETA es 'MUEVE_AQUI' y el DOCUMENTO 'source.py'\n")
    print("CONSEJO 2: Para fines de actividad recomendamos que el archivo que copies lo MUEVAS al directorio 'MUEVE_AQUI'\n")
    print(f"En {segundos} segundos se actualizara la carpeta de archivos\n")
    time.sleep(segundos)
    for raiz, dirs, archivos in os.walk(".", topdown=False):
        for nombre in archivos:
            print(os.path.join(raiz, nombre))
        for nombre in dirs:
            print(os.path.join(raiz, nombre))
            respuesta_mover = "si"
            
            while respuesta_mover == "si":
                mover_doc = input("\n¿Que documento quieres mover?: ")
                directorio = input("Escribe correctamente el directorio al que quieres mover el documento: ")
                shutil.move(mover_doc, directorio, copy_function = shutil.copy)
                print("se ejecuto correctamente")
                respuesta_mover = input("¿Quieres Mover algun otro archivo? 'si' 'no':\n ")
                if respuesta_mover == "no":
                    print(separador)
                    print("Estos son los documentos y archivos ACTUALIZADOS: \n")
                    print(f"En {segundos} segundos se actualizara la carpeta de archivos\n")
                    time.sleep(segundos)
                    for raiz, dirs, archivos in os.walk(".", topdown=False):
                        for nombre in archivos:
                            print(os.path.join(raiz, nombre))
                        for nombre in dirs:
                            print(os.path.join(raiz, nombre))
                    print("\nFin del punto numero 3.1")
                    print(separador)

if eleccion == 3:
    import random
    loop = 1
    dado= [1,2,3,4,5,6,7,8,9,10,11,12]
    print(separador +"\n")
    respuestas_validas=["si","SI","Si","sI"]
    while loop == 1:
        print(f"Estas son los lados del dado: ")
        print(*dado)
        jugadores= int(input("Dime cuantos jugadores van a tirar el dado "))
        print("Se procede a lanzar el dado creado\n")
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
if eleccion == 5:
    
    import random
    import time
    import sys
    contador = 1
    separador = ("×" * 25)
    print(separador +"\n")
    
    while contador == 1:
        eleccion2 = int(input("Selecciona el numero que deseas realizar primero\n 1.Entrar a ejemplo de lista\n 2.Entrar a ejemplo de Tupla\n 3.Solo si ya se ejecutaron las 2 anteriores solamente 1 vez para ver sus diferencias\n"))
        print(separador +"\n")
        if eleccion2 == 1:
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
                inicio_L = time.time()
                for turno in range(jugadores):
                    print(f"Este es el resulado: {random.choice(dado)}")
                    print(separador +"\n")
                    final_L = time.time()
                continuar = str(input("Si desean tirar el dado de nuevo escribe\n Si\n No\n"))
                print(separador +"\n")
                if continuar in respuestas_validas :
                    print("Nice")
                    print(separador +"\n")
                else:
                    print("Vuelve pronto crack")
                    loop = 2
                    print(separador +"\n")

        if eleccion2 == 2:
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
                inicio_T = time.time()
                for turno in range(jugadores):
                    print(f"Este es el resulado: {random.choice(dadoT)}")
                    print(separador +"\n")
                    final_T = time.time()
                continuar = str(input("Si desean tirar el dado de nuevo escribe\n Si\n No\n"))
                print(separador +"\n")
                if continuar in respuestas_validas :
                    print("Nice")
                    print(separador +"\n")
                else:
                    print("Vuelve pronto crack")
                    loop = 2
                
        if eleccion2 ==3:
            print(separador +"\n")
            duracion_L = (final_L - inicio_L)
            lista = dado
            duracion_T = (final_T - inicio_T)
            tupla = dadoT
            print(f"La lista tiene {len(lista)} elementos, y tiene un tamaño de {sys.getsizeof(lista)} bytes")
            print(f"La tupla tiene {len(tupla)} elementos, y tiene un tamaño de {sys.getsizeof(tupla)} bytes")
            print(f"La duracion en la ejecucion del programa de lista fue {duracion_L} segundos")
            print(f"La duracion en la ejecucion del programa de tupla fue de {duracion_T} segundos")
            contador = 2






