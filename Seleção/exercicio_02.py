# 2) Escreva um programa que leia as notas das duas avaliações normais e a nota da avaliação optativa.
# Caso o aluno não tenha feito a optativa deve ser fornecido o valor -1. Calcular a média do semestre
# considerando que a prova optativa substitui a nota mais baixa entre as duas primeiras avaliações.
# Escrever a média e mensagens que indiquem se o aluno foi aprovado, reprovado ou está em exame, de
# acordo com as informações abaixo:
# Aprovado : média >= 6.0 Reprovado: media < 3.0 Exame: média >= 3.0 e < 6.0

n1 = float(input("Qual é a mota da P1: "))
n2 = float(input("Qual é a mota da P2: "))

media = (n1 + n2)/2

if media >= 6:
    print("Aprovado")
elif media < 6:
    respota = str(input("O aluno fez a prova optativa? (S ou N)")).lower()
    if respota == 's':
        po = float(input("Qual é a mota da PO: "))
    else:
        po = -1

    if n1 > n2:
        n2 = po
    else:
        n1 = po

    media = (n1 + n2)/2

    if media >= 6:
        print("Aprovado")
    else:
        print("Reprovado")
