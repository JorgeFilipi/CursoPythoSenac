# 19) Escreva um programa para ler 3 valores e escrever a soma dos 2 maiores. Considere que o usuário
# não informará valores iguais

n1 = int(input("Digite um número inteiro: "))
n2 = int(input("Digite um número inteiro: "))
n3 = int(input("Digite um número inteiro: "))

if n1 > n2 and n1 > n3 and n2 > n3:
    print(n1 + n2)
elif n1 > n2 and n1 > n3 and n3 > n2:
    print(n1 + n3)
elif n2 > n1 and n2 > n3 and n1 > n3:
    print(n2 + n1)
elif n2 > n1 and n2 > n3 and n3 > n1:
    print(n2 + n3)
elif n3 > n1 and n3 > n2 and n1 > n2:
    print(n3 + n1)
elif n3 > n1 and n3 > n2 and n2 > n1:
    print(n3 + n2)
