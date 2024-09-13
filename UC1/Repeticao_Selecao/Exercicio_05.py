# 5) Escreva um programa para ler as notas da 1a e 2a avaliações de um aluno, calcular e imprimir a
# média semestral. Faça com que o algoritmo só aceite notas válidas (uma nota válida deve pertencer ao
# intervalo [0,10]). Cada nota deve ser validada separadamente. Deve ser impressa a mensagem "Nota
# inválida" caso a nota informada não pertença ao intervalo [0,10].

nota1 = float(input("\nInforme a 1ª nota do aluno: "))

while True:

    if 0 <= nota1 <= 10:
        break
    else:
        nota1 = float(input("Nota inválida. Tente novamente: "))


nota2 = float(input("\nInforme a 2ª nota do aluno: "))

while True:

    if 0 <= nota2 <= 10:
        break
    else:
        nota2 = float(input("Nota inválida. Tente novamente: "))

media = (nota1 + nota2) / 2

if media >= 6:
    resultado = "APROVADO, Parabéns!"
else:
    resultado = "REPROVADO, Estude mais!"

print(f"\nA média semestral é: {media:.2f}\n", resultado, "\n")
