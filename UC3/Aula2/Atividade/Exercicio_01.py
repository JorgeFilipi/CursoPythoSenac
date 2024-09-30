# Exercício 1: Função de Cálculo do Fatorial
#
# Objetivo: Criar uma função que calcule o fatorial de um número dado.
#
# - Descrição: Peça ao usuário para inserir um número e use uma função para calcular e retornar o fatorial desse número. O fatorial de um número não negativo ( n ),
# denotado por ( n! ), é o produto de todos os números positivos menores ou iguais a ( n ).


def fatorial(fat):
    fat = 1
    if num == 0 or num == 1:
        return  fat
    if num >= 2:
        for i in range(1, num + 1):
            fat = fat * i
        return fat



num = int(input("Digite um número: "))
print(f"O fatorial de {num} é {fatorial(num)}.")
