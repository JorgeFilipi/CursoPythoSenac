# 3) Escreva um programa para ler as notas das duas avaliações de um aluno no semestre, calcular e
# escrever a média semestral e a seguinte mensagem: PARABÉNS! Você foi aprovado! somente se o
# aluno foi aprovado (considere 6.0 a média mínima para aprovação).

n1 = float(input("Qual é a mota da P1: "))
n2 = float(input("Qual é a mota da P2: "))

media = (n1 + n2)/2

if media >= 6:
    print("PARABÉNS!")
else:
    print("Voçê esta reprovado!")
