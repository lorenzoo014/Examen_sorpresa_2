#lanzador
from Ejercicios import Ejercicio1,Ejercicio2,Ejercicio3, tabla #importacion de los modulos
from Ejercicios.Ejercicio1 import Ejercicio1  #importacion
# from Ejercicios.Ejercicio2 import Ejercicio2  #de
# from Ejercicios.Ejercicio3 import Ejercicio3  #las
from Ejercicios.tabla import tabla            #clases







def pruebas():
    matriz = [
    [1,1,1,3],
    [2,2,2,7],
    [3,3,3,9],
    [4,4,4,13],
    ]
    print(Ejercicio1.sumaMatrices(matriz))

if __name__ == "main":
    pruebas() 