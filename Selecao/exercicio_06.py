# 6) Reescreva o programa do exercício anterior considerando o zero como neutro, ou seja, se for
# digitado o valor zero, escrever a palavra zero.

n = int(input("Qual o valor você quer testar? "))

if n > 0:
    print("Este número é positivo!")
elif n < 0:
    print("Este número é negativo")
else:
    print("Você digitou o número '0'!")
