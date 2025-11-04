dados = {"nome": "Rafaella", "idade": 28, "telefone": "1234-1234"}

# acessar pela chave
print(dados["nome"])  # "Rafaella"
print(dados["idade"])  # 28
print(dados["telefone"])  # "3333-1234"
# atribuir novos valores 
dados["nome"] = "Maria"
dados["idade"] = 18
dados["telefone"] = "9988-1781"

print(dados)  # {"nome": "Maria", "idade": 18, "telefone": "9988-1781"}