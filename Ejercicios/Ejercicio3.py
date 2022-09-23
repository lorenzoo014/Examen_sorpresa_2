class Ejercicio3:
    def añadeElementos(primerElemento,segundElemento,avance=1):
        lista1=[]
        for element in range(primerElemento,segundElemento,avance):
            lista1.append(element)
        return lista1


    def añadeElementos2(primerElemento,segundoElemento,avance=1):
        primerElemento+=avance
        segundoElemento-=avance
        lista1=[]

        
        if(segundoElemento==0):
            return lista1
        lista1.append(primerElemento)
        añadeElementos2(primerElemento,segundoElemento)



# lista1=[]
# lista2=[]
# lista3=[]
# lista4=[]
# lista5=[]

# for element in range(0,11):
#     lista1.append(element)
# print(lista1)

# for element in range(-10,1):
#     lista2.append(element)

# for element in range(0,21,2):
#     lista3.append(element)
# print(lista3)

# for element in range(-19,0,2):
#     lista4.append(element)
# print(lista4)

# for element in range(0,51,5):
#     lista5.append(element)
# print(lista5)