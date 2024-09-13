# 48) Elaborar um algoritmo em pseudocodigo que efetue a leitura de um número inteiro e
# apresentar uma mensagem informando se o número é par ou ímpar.

num = int(input("Digite um número: "))

if num % 2 == 0:
    print(num, "Este número é par!")
else:
    print(num, "Este número é impar!")
