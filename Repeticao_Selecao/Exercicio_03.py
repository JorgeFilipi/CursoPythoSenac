# 3) Reescreva o programa para o exercício 1 utilizando a estrutura Enquanto/Faça na construção da
# repetição de validação.

n1 = float(input("Escreva um número: "))
cond = True

while cond:
    n2 = float(input("Escreva outro número diferente de zero: "))
    if n2 != 0:
        cond = False

print(n1 * n2)
