# 18) Escreva um programa para ler 3 valores inteiros e escrever o maior deles. Considere que o usuário
# não informará valores iguais.


n1 = int(input("Digite um número inteiro: "))
n2 = int(input("Digite um número inteiro: "))
n3 = int(input("Digite um número inteiro: "))

if n1 > n2 and n1 > n3:
    print(n1)
elif n2 > n1 and n2 > n3:
    print(n2)
else:
    print(n3)
