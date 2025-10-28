# Operadores Lógicos
# São operadores utilizados em conjunto com os operadores de comparação, para montar uma expressão lógica.

# Operador E
saldo = 1000
saque = 200
limite = 100
saldo >= saque and saque <= limite
# >>> False

# Operador OU
saldo = 1000
saque = 200
limite = 100
saldo >= saque or saque <= limite
# >>> True

# Operador Negação
contatos_emergencia = []
not 1000 > 1500
# >>> True
not contatos_emergencia
# >>> True
not "saque 1500;"
# >>> False
not ""
# >>> False