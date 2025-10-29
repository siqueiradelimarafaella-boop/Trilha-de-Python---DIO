saldo = 2000
saque = 500


status = "Sucesso" if saldo >= saque else "Falha"

print(f"{status} ao realizar o saque!")

# Bom para verificações rápidas e simples.
# modificar os valores de saldo e saque para testar as condições.