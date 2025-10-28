# int para float
preco = 10
print(preco)

preco= float(preco)
print(preco)

preco = 10/2
print (preco)

# float para int
preco = 10.3
print(preco)

preco= int(preco)
print(preco)

# conversão por divisão
preco = 10
print(preco)
preco = 10/2
print (preco)
preco = 10//2  
print (preco)
# Se fazer a divisão com duas barras, ele preserva o número inteiro

# numérico para string
preco = 10.3
idade = 28
print(str(preco))
print(str(idade))
# visualmente não tem diferença, mas transforma o número em texto
texto = f"idade  {idade} preco {preco}"
print(texto)
# concatenar string com variáveis (precisa colocar entre chaves)

# string para números
preco = 10.3
idade = 28
print(int(preco))
print(float(idade))

# Erro de conversão
# nem sempre é possível converter um tipo para o outro
# não é possível converter uma string para float ou int (querer transformar uma palavra em um número)