while True:
    numero = int(input("Informe um número: "))

    if numero == 10:
        break

    if numero % 2 == 0:
        continue

    print(numero)
# Vai repetir até a condição ser atendida, neste caso o número precisa ser 10 para finalizar o programa


# Essa estrutura pode ser feita com for também
# Programa que exibe apenas os números impares. Enquanto o número for par, ele vai pulando 
for num in range(100):

    if num % 2 == 0:
        continue

    print(num, end=" ")

    # variação do break, continue