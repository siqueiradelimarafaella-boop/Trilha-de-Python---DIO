salario = 2000 #está num escopo global


def salario_bonus(bonus):
    global salario  #chamamos a variável
    salario += bonus
    return salario


salario_bonus(500)  # 2500