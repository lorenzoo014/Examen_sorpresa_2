
#----------------1er_Ej.----------------#
argumento1 = input("Introduce un numero ")        #filas
argumento2= input("Introduce un segundo numero ") #columnas


try:
    argumento2= int(argumento2)
    argumento1= int(argumento1)
except:
    print("SE TIENEN QUE INTRODUCIR NUMEROS")

assert argumento1<10 ,"Introduce un numero entre el 1 y el 10"
assert argumento2<10 ,"Introduce un numero entre el 1 y el 10"


#----------------2do_Ej.----------------#
# argumento1=5 #filas
# argumento2=3 #columnas

for i in range (0,argumento1+1):
    for i in range (0,argumento2+1):
        print("*", end="")

for i in range (0,argumento1):
    print("")#cambio de linea
    for i in range (0,argumento2):
        print("*", end="")


# assert (type(argumento1) == int or int(argumento1)<10 or int(argumento2)<10), "Introduce un numero de verdad"



# space = 2
# for i in range(1,6,2):
#     print(space*' '+i*'*')
#     space = space-1