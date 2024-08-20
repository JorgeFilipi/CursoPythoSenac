# 10) Escreva um programa para ler 3 valores inteiros (considere que não serão lidos valores iguais) e
# escrevê-los em ordem crescente.

# solução com lista

n1 = int(input("Digite um número inteiro: "))
n2 = int(input("Digite um número inteiro: "))
n3 = int(input("Digite um número inteiro: "))
list = [n1, n2, n3]

print(sorted(list))
