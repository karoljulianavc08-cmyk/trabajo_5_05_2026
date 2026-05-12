print("Holaaaaaa Bienvenido a nuestro programa ")

#Esta variable es la que guarda la opcion qude el usuario elija
opciones = 0

#Mientras la opcion es diferente a 3 puede seguir con el menú.
while opciones != 3:
    print("MENÚ PRINCIPAL") #Imprime "menú principal"
    print("1. Operaciones") # Esta opción va a ser para poder hacer opciones
    print("2. Mensajes") #Esta opción va a imprimir mensajes
    print("3. Salir") #Esta opción es para salir del programa

    opciones = int(input("Elige una opción: ")) #Aqui el usuario puede elegir la opcion que quiera

    # SUBMENÚ 1, para hacer las operaciones
    while opciones == 1:
        sub = 0
        while sub != 3:
            print("SUBMENÚ OPERACIONES") #Solo imprime submenú operaciones
            print("1. Sumar") #Esta opcion es para sumar numeros
            print("2. Restar") #Esta opcion es para restar numeros
            print("3. Volver") #Esta opcion es para volver al menú principal

            sub = int(input("Elige una opción: ")) # Esto es para que pueda elegir si quiere sumar, restar o volver.

            if sub == 1: #si se elige la opción sumar, se piden 2 numeros y los suma.
                print("Este programa es para sumer 2 numeros")
                a = int(input("Número 1: "))
                b = int(input("Número 2: "))
                print("Resultado:", a + b)

            elif sub == 2: #si se elige esta opción, se piden 2 numeros y se restan.
                print("Este programa es para restar 2 numeros")
                a = int(input("Número 1: "))
                b = int(input("Número 2: "))
                print("Resultado:", a - b)

        break

    # SUBMENÚ 2 para mandar un mensaje.
    while opciones == 2:
        sub = 0
        while sub != 2:
            print("SUBMENÚ MENSAJES") #solo imprime submenú mensajes.
            print("1. Palabras") #Esta opcion es para seguir con las palabras 10 veces repetidas.
            print("2. Volver") #Con esta opcion vuelve al menú principal.

            sub = int(input("Elige una opción: ")) #Aqui tiene que elegir la opcion 

            if sub == 1:
                print("Esta opcion es para imprimir una palabra 10 veces") #Imprime esta frase.

                palabra= input("ingrese una palabra que quiera repetir 10 veces por favor: ") #se ingresa la palabra o frase. 
                for i in range(10):
                 print("Su palabra es:", palabra ) #se imprime la palabra o frase.
                

        break


print("Programa terminado")