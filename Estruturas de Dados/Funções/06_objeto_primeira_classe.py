def somar(a, b):
    return a + b


def exibir_resultado(a, b, funcao):
    resultado = funcao(a, b)
    print(f"O resultado da operação de {a} + {b} = {resultado}")


exibir_resultado(10, 10, somar)  # O resultado da operação de 10 + 10 = 20
