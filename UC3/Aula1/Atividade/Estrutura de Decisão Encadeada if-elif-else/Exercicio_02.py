# 2. Questão 2: Avaliação Escolar
#    - Enunciado: Escreva um programa que peça a nota final de
# um aluno e o classifique em 'Excelente', 'Bom', 'Satisfatório', 'Insuficiente',
# usando uma estrutura de decisão encadeada.
# Código Inicial:
# nota = float(input("Digite a nota do aluno: "))

nota = float(input("Digite a nota do aluno: "))

if 8.5 <= nota <= 10.0:
    print("Excelente!")
elif 7.0 <= nota < 8.5:
    print("Bom!")
elif 5.0 <= nota < 7.0:
    print("Satisfatório!")
else:
    print("Insuficiente!")