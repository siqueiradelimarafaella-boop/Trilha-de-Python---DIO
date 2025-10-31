nome = "rafaElla"

# Maiuscula
print(nome.upper())
# Minuscula 
print(nome.lower())
# Converte todas as letras em minusculo, menos a primeira letra
print(nome.title())



texto = "  Bom dia!    "
# Juncao de string com caracter 
print(texto + ".")
# Elimina o espa;o em branco de todos os lados
print(texto.strip() + ".")
# Elimina o espa;o em branco da direita
print(texto.rstrip() + ".")
# Elimina o espa;o em branco da esquerda
print(texto.lstrip() + ".")


# Junção de string+caracter e centralização
curso = "Python"

print("####" + curso + "####")
print(curso.center(14))
print(curso.center(14, "#"))
print("-".join(curso))

# INTERPOLAÇÃO
nome = "Rafaella"
idade = 28
profissao = "Progamadora"
linguagem = "Python"
saldo = 70.900

dados = {"nome": "Rafaella", "idade": 28}

# Utilizando %
print("Nome: %s Idade: %d" % (nome, idade))
# utiliza %s para strings, %d para valores inteiros e %f para valores de ponto flutuante
# No final % (argumento). Necessário manter a ordem de acordo com o uso

# Metodo format
print("Nome: {} Idade: {}".format(nome, idade))
# utiliza as chaves para indicar onde a informação deve ficar
# Ainda é necessário manter a ordem

print("Nome: {1} Idade: {0}".format(idade, nome))
print("Nome: {1} Idade: {0} Nome: {1} {1}".format(idade, nome))
# Nesse caso, enumerando, adicionamos a informação de acordo com a posição 

print("Nome: {nome} Idade: {idade}".format(nome=nome, idade=idade))
print("Nome: {name} Idade: {age} {name} {name} {age}".format(age=idade, name=nome))
print("Nome: {nome} Idade: {idade}".format(**dados))
# Forma para melhorar a legibilidade do código

# Método f
print(f"Nome: {nome} Idade: {idade}")
print(f"Nome: {nome} Idade: {idade} Saldo: {saldo:.2f}")
# tamanho do que será exibido
print(f"Nome: {nome} Idade: {idade} Saldo: {saldo:10.1f}")
# adiciona espaço antes da informação

# FATIAMENTO
# (start, stop, step)
nome = "Rafaella Siqueira de Lima"

print(nome[0])
# pega o primeiro item
print(nome[-2])
# retorna de trás para frente
print(nome[:9])
# retorna o descrito em 9 posições
print(nome[10:])
# A partir de 10 até o final da string
print(nome[10:16])
# Pegar um pedaço da string
print(nome[10:16:2])
# Utiliza o passo, vai pegando as letras, no espaçamento definido (2)
print(nome[:])
# Retorna a string inteira
print(nome[::-1])
# Espelha a string

# STRING DE MÚLTIPLAS LINHAS
# util para formatação do texto

nome = "Rafaella"

mensagem = f"""
   Olá meu nome é {nome},
 Eu estou aprendendo Python.
     Essa mensagem tem diferentes recuos.
"""

print(mensagem)


print(
    """
    ============= MENU =============

    1 - Depositar
    2 - Sacar
    0 - Sair

    ================================

            Obrigado por usar nosso sistema!!!!
"""
)