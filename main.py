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
            tabla.crearTabla("")






        if opcion == '6':
 print("Saliendo...\n")
break
input("\nPresiona ENTER para continuar...")


if __name__ == "main":
    pruebas() 

    
def iniciar():
   while True:
     print("========================")
     print(" BIENVENIDO AL Manager ")
     print("========================")
     print("[1] Listar clientes ")
     print("[2] Buscar cliente ")
     print("[3] Añadir cliente ")
     print("[4] Modificar cliente ")
     print("[5] Borrar cliente ")
     print("[6] Cerrar el Manager ")
     print("========================")
     opcion = input("> ")
     os.system('clear') # cls en Windows
  if opcion == '1':
   print("Listando los clientes...\n")
   for cliente in db.Clientes.lista:
     print(cliente)
  if opcion == '2':
   print("Buscando un cliente...\n")
   dni = helpers.leer_texto(3, 3, "DNI (2 ints y 1 char)").upper()
   cliente = db.Clientes.buscar(dni)
   print(cliente) if cliente else print("Cliente no encontrado.")
  if opcion == '3':
    if opcion == '3':
 print("Añadiendo un cliente...\n")
 # Comprobación de DNI válido
 while 1:
 dni = helpers.leer_texto(3, 3, "DNI (2 ints y 1
char)").upper()
 if helpers.dni_valido(dni, db.Clientes.lista):
 break
 nombre = helpers.leer_texto(
 2, 30, "Nombre (de 2 a 30 chars)").capitalize()
 apellido = helpers.leer_texto(
 2, 30, "Apellido (de 2 a 30 chars)").capitalize()
 db.Clientes.crear(dni, nombre, apellido)
if opcion == '4':
 print("Modificando un cliente...\n")
 dni = helpers.leer_texto(3, 3, "DNI (2 ints y 1 char)").upper()
 cliente = db.Clientes.buscar(dni)
 if cliente:
   nombre = helpers.leer_texto(
     2, 30, f"Nombre (de 2 a 30 chars)[{cliente.nombre}]").capitalize()
   apellido = helpers.leer_texto( 2, 30, f"Apellido (de 2 a 30 chars)[{cliente.apellido}]").capitalize()
   db.Clientes.modificar(cliente.dni, nombre, apellido)
   print("Cliente modificado correctamente.")
 else:
   print("Cliente no encontrado.")
if opcion == '5':
 print("Borrando un cliente...\n")
 dni = helpers.leer_texto(3, 3, "DNI (2 ints y 1 char)").upper()
 print("Cliente borrado correctamente.") if db.Clientes.borrar(
 dni) else print("Cliente no encontrado.")
