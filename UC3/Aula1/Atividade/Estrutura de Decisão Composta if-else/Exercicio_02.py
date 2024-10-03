# 2. Questão 2: Par ou Ímpar
#    - Enunciado: Solicite um número do usuário e use `if-else`
# para determinar se o número é par ou ímpar. Imprima o resultado apropriado.
# Código Inicial:
# numero = int(input("Digite um número: "))

num = int(input('Digite um número para verifier se é par ou impar: '))

if num % 2 == 0:
    print("par")
else:
    print("impar")
