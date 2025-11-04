contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},
    "giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3443-2121"},
    "chappie@gmail.com": {"nome": "Chappie", "telefone": "3344-9871"},
    "melaine@gmail.com": {"nome": "Melaine", "telefone": "3333-7766"},
}
# primeira chave esta acessando o contato (que é o e-mail com uma lista atribuida, atribuida a outro dicionario)
telefone = contatos["giovanna@gmail.com"]["telefone"]  # "3443-2121"
print(telefone)