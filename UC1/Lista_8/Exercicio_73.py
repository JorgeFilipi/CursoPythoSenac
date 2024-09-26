# 73) Faça um algoritmo que determine o maior entre N números. A condição de parada é a
# entrada de um valor 0, ou seja, o algoritmo deve processar o maior até que a entrada seja igual a
# 0 (ZERO).

maior = 0
voltas = 1

while True:
    num = int(input("Digite um número para comparação: "))
    voltas += 1
    if maior < num:
        maior = num
        print(f"Este é o maior número {maior}")
    elif num == 0:
        print(f"Você digitou {voltas}, números")
        print("Fim do programa!")
        break
    else:
        print(f"Este ainda é maior número: {maior}")
