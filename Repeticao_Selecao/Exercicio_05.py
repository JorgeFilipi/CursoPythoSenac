# 5) Escreva um programa para ler as notas da 1a e 2a avaliações de um aluno, calcular e imprimir a
# média semestral. Faça com que o algoritmo só aceite notas válidas (uma nota válida deve pertencer ao
# intervalo [0,10]). Cada nota deve ser validada separadamente. Deve ser impressa a mensagem "Nota
# inválida" caso a nota informada não pertença ao intervalo [0,10].

nota1 = float(input("Informe a 1ª nota do aluno: "))
test = True
while test:

    if 0 <= nota1 <= 10:
        test = False
    else:
        nota1 = float(input("Nota inválida. Tente novamente: "))


nota2 = float(input("Informe a 2ª nota do aluno: "))
test = True
while test:

    if 0 <= nota2 <= 10:
        test = False
    else:
        nota2 = float(input("Nota inválida. Tente novamente: "))

media = (nota1 + nota2) / 2

print(f"A média semestral é: {media:.2f}")
