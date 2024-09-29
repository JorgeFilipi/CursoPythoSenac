# Exercício 1: Função de Cálculo do Fatorial
#
# Objetivo: Criar uma função que calcule o fatorial de um número dado.
#
# - Descrição: Peça ao usuário para inserir um número e use uma função para calcular e retornar o fatorial desse número. O fatorial de um número não negativo ( n ),
# denotado por ( n! ), é o produto de todos os números positivos menores ou iguais a ( n ).


def fatorial(n):
    if n == 0:
        return 1
    else:
        return n * fatorial(n-1)


numero = int(input("Digite um número: "))
print(f"O fatorial de {numero} é {fatorial(numero)}.")
