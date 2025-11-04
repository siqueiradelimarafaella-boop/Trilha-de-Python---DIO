carros = ["gol", "celta", "palio"]

for carro in carros:
    print(carro)
# Vamos passar cada item, pra variável do for

for indice, carro in enumerate(carros):
    print(f"{indice}: {carro}")