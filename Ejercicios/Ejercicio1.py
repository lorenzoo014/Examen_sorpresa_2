
class Ejercicio1():
    def sumaMatrices(matriz):        
        # matriz = [
        # [1,1,1,3],
        # [2,2,2,7],
        # [3,3,3,9],
        # [4,4,4,13],
        # ]

        for element in matriz:
            # print(matriz[2:1:-1])
            if (element[-1]) == sum(element)-element[-1]:
                pass
            else:
                element[-1] = sum(element)-element[-1]

        return matriz


        #hay que hacer lo de toca si es ejercicio 1