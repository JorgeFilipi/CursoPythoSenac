# 1. Questão 1: Classificação por Faixa Etária
#    - Enunciado: Peça a idade do usuário e classifique-o em categorias
# ('Criança', 'Adolescente', 'Adulto', 'Idoso') usando "if-elif-else".
# Código Inicial:
# idade = int(input("Digite sua idade: "))

idade = int(input("Digite sua idade: "))
if idade >= 60:
    print("idoso!")
elif 60 > idade >= 25:
    print("Adulto")
elif 25 > idade >= 12:
    print("Adolescente")
else:
    print("Criança")