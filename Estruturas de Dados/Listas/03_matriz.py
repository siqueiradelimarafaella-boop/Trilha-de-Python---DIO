matriz = [
    [1, "a", 2],
    ["b", 3, 4],
    [6, 5, "c"]
]

print(matriz[0])  # [1, "a", 2] , pegar o valor de uma linha
print(matriz[0][0])  # 1 precisa informar o valor da linha e da coluna
print(matriz[0][-1])  # 2 utilizar o indice negativo na coluna
print(matriz[-1][-1])  # "c" utilizar o indice negativo tanto na linha como na coluna