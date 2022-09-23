matriz = [
[1,1,1,3],
[2,2,2,7],
[3,3,3,9],
[4,4,4,13],
]
print(matriz)

for element in matriz:
    # print(matriz[2:1:-1])
    if (element[-1]) == sum(element)-element[-1]:
        pass
    else:
        element[-1] = sum(element)-element[-1]

print(matriz)