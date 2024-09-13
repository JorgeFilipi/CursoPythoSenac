# 12) Tendo como entrada a altura e o sexo (codificado da seguinte forma: 1:feminino 2:masculino) de
# uma pessoa, construa um programa que calcule e imprima seu peso ideal, utilizando as seguintes
# fórmulas:
# - para homens : (72.7 * h) – 58
# - para mulheres : (62.1 * h) – 44.7
# Observação: Altura = h (na fórmula acima).

altura = float(input("Qual é a sua altura? "))
sexo = int(input("Qual o seu sexo? '1:feminino 2:masculino' "))

if sexo == 2:
    peso = (72.7*altura)-58
    print(f"O peso ideal para homem com essa {altura} é {peso:,.2f}")
else:
    peso = (62.1*altura)-44.7
    print(f"O peso ideal para mulher com essa {altura} é {peso:,.2f}")
