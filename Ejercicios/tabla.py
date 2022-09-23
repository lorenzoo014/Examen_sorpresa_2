

class tabla():
    #----------------1er_Ej.----------------#
    def crearTabla(filas="k", columnas="k"):                
        try:
            columnas= int(columnas)
            filas= int(filas)
        except:
            print("Informacion acerca del Script:" + "\n" + 
            "se debe utilizar dos argumentos, uno que sean filas y otro que sean columnas" + "\n" +
            "si no se introduce algo de lo especificado  y de la forma especificada seguirá dando error"
            )

        assert filas<10 ,"Introduce un numero entre el 1 y el 9"
        assert columnas<10 ,"Introduce un numero entre el 1 y el 9"


        #----------------2do_Ej.----------------#

        print("--------TODO_FILAS--------")
        for i in range (0,filas+1):
            for i in range (0,columnas+1):
                print("*", end="")
        print("\n")
        print("--------RECTANGULO--------")

        for i in range (0,filas):
            print("")#cambio de linea
            for i in range (0,columnas):
                print("*", end="")
        print("")
        print("La ultima se considera la tabla final")

# assert (type(argumento1) == int or int(argumento1)<10 or int(argumento2)<10), "Introduce un numero de verdad"

