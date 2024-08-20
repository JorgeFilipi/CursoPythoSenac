# 10) Escreva um programa para ler 3 valores inteiros (considere que não serão lidos valores iguais) e
# escrevê-los em ordem crescente.

# solução com infinitos if

n1 = int(input("Digite um número inteiro: "))
n2 = int(input("Digite um número inteiro: "))
n3 = int(input("Digite um número inteiro: "))

if n1 < n2 and n1 < n3 and n2 < n3:
    print(f'A ordem crescente é {n1} , {n2} e {n3}')
elif n1 < n2 and n1 < n3 and n3 < n2:
    print(f'A ordem crescente é {n1} , {n3} e {n2}')
elif n2 < n1 and n2 < n3 and n1 < n3:
    print(f'A ordem crescente é {n2} , {n1} e {n3}')
elif n2 < n1 and n2 < n3 and n3 < n1:
    print(f'A ordem crescente é {n2} , {n3} e {n1}')
elif n3 < n1 and n3 < n2 and n1 < n2:
    print(f'A ordem crescente é {n3} , {n1} e {n2}')
elif n3 < n1 and n3 < n2 and n2 < n1:
    print(f'A ordem crescente é {n3} , {n2} e {n1}')
