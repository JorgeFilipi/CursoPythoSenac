# 2) Altere a solução do exercício anterior para que seja impressa a mensagem Valor inválido! caso o
# segundo valor informado seja zero.

n1 = float(input("Escreva um número: "))
cond = True

while cond:
    n2 = float(input("Escreva outro número diferente de zero: "))
    if n2 != 0:
        cond = False
    else:
        print("Valor inválido!")
print(n1 / n2)
