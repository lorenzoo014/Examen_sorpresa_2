#lanzador
from Ejercicios import Ejercicio1,Ejercicio2,Ejercicio3, tabla #importacion de los modulos
from Ejercicios.Ejercicio1 import Ejercicio1  #importacion
from Ejercicios.Ejercicio2 import Ejercicio2  #de
from Ejercicios.Ejercicio3 import Ejercicio3  #las
from Ejercicios.tabla import tabla            #clases







def pruebas():
    matriz = [
    [1,1,1,3],
    [2,2,2,7],
    [3,3,3,9],
    [4,4,4,13],
    ]
    while True:
        print("========================")
        print(" BIENVENIDO AL Manager ")
        print("========================")
        print("[1] Ejercicio_1 ")
        print("[2] Ejercicio_2 ")
        print("[3]  Ejercicio_3 ")
        print("[4]  Ejercicio_4 ")
        print("[5] Cerrar el Manager ")
        print("========================")
        opcion = input("> ")
        if opcion == '1':
            print("Ejercicio_1 con la siguiente matriz...\n")
            print("[1,1,1,3]")
            print("[2,2,2,7]")
            print("[3,3,3,9]")
            print("[4,4,4,13]")
            print(Ejercicio1.sumaMatrices(matriz))
        if opcion == "2":
            print("Ejercicio_2 con los siguientes strings...\n")
            print("Hola")
            print("nochevieja")
            print("fun__fun__fun")
            print("adios")
            Ejercicio2.Ejericio2.cadena("Hola")
            Ejercicio2.Ejericio2.cadena("nochevieja")
            Ejercicio2.Ejericio2.cadena("fun__fun__fun")
            Ejercicio2.Ejericio2.cadena("adios")

        if opcion == "3":
            print("Ejercicio_3 ...\n")
            print("del 0 al 10")
            Ejercicio3.añadeElementos2(0,10)
            print("del -10 al 0")
            Ejercicio3.añadeElementos2(-10,0)
            print("del 0 al 20 pares")
            Ejercicio3.añadeElementos2(0,10,2)
            print("del -20 al 0")
            Ejercicio3.añadeElementos2(-19,0,2)
            print("del 0 al 50")
            Ejercicio3.añadeElementos2(0,50,5)
        if opcion == "4":
            print("Ejercicio_4 ...\n")
            tabla.crearTabla(5,5)

        if opcion == '5':
            print("Saliendo...\n")
            break
input("\nPresiona ENTER para continuar...")

