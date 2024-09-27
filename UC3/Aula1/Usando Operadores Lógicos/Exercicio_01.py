# 1. Questão 1: Múltiplas Condições
#    - Enunciado: Verifique se um número é positivo e par.
# Solicite um número ao usuário e imprima se ele satisfaz ambas as condições.
# Código Inicial:
# numero = int(input("Digite um número: "))

num = int(input("Digite um número: "))

if num >= 0:
    if num % 2 == 0:
        print("Número par e positivo! ")