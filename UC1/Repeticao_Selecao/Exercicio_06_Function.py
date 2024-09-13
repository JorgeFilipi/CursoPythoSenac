# 5) Escreva um programa para ler as notas da 1a e 2a avaliações de um aluno, calcular e imprimir a
# média semestral. Faça com que o algoritmo só aceite notas válidas (uma nota válida deve pertencer ao
# intervalo [0,10]). Cada nota deve ser validada separadamente. Deve ser impressa a mensagem "Nota
# inválida" caso a nota informada não pertença ao intervalo [0,10].
#
#  6) Reescreva o programa para o exercício 5 para que no final seja impressa a mensagem Novo cálculo
#  (1.sim 2.não) solicitando ao usuário que informe um código (1 ou 2) indicando se ele deseja ou não
#  executar o programa novamente. Se for informado o código 1 deve ser repetida a execução de todo o
#  programa para permitir um novo cálculo, caso contrário ele deve ser encerrado.


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

    nome = str(input("\nQual o nome do aluno: ").title())
    if media >= 6:
        return nome + " APROVADO, Parabéns!"
    else:
        return nome + " REPROVADO, Estude mais!"


def nota():

    print("\nNota 1\n")
    nota1 = lerNota()
    print("\nNota 2\n")
    nota2 = lerNota()

    media = calculoMedia(nota1, nota2)

    print(f"\n\nA média semestral é: {
          media:.2f}: aluno", definorResultado(media))


while tuple:
    resposta = int(input("\n\nDidite 1 para continuar ou 2 para sair: "))
    if resposta == 1:
        nota()
    elif resposta == 2:
        break
    else:
        print("Resposta errada digite 1 ou 2 apenas\n")
