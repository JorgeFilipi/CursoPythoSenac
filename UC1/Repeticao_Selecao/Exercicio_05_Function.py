# 5) Escreva um programa para ler as notas da 1a e 2a avaliações de um aluno, calcular e imprimir a
# média semestral. Faça com que o algoritmo só aceite notas válidas (uma nota válida deve pertencer ao
# intervalo [0,10]). Cada nota deve ser validada separadamente. Deve ser impressa a mensagem "Nota
# inválida" caso a nota informada não pertença ao intervalo [0,10].

def lerNota():

    while True:
        try:
            nota = float(input("Digite a nota (0 a 10): "))
            if 0 <= nota <= 10:
                return nota
            else:
                print("Nota inválida. Tente novamente: ")
        except ValueError:
            print("Entrada inválida. Digite um número.")


def calculoMedia(nota1, nota2):

    return (nota1 + nota2) / 2


def definorResultado(media):

    if media >= 6:
        return "APROVADO, Parabéns!"
    else:
        return "REPROVADO, Estude mais!"


# Ler as notas
print("\nNota 1\n")
nota1 = lerNota()
print("\nNota 2\n")
nota2 = lerNota()

# Calcular a média
media = calculoMedia(nota1, nota2)

# Imprimir a média

print(f"\n\nA média semestral é: {media:.2f}", definorResultado(media))
