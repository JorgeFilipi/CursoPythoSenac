# 73) Faça um algoritmo que determine o maior entre N números. A condição de parada é a
# entrada de um valor 0, ou seja, o algoritmo deve processar o maior até que a entrada seja igual a
# 0 (ZERO).

maior = 0
cont = -1

while True:
    num = int(input("Digite um número inteiro: "))
    cont = cont + 1
    if maior < num:
        maior = num

    if num == 0:
        break

print(f"O maior número digitado foi {maior}")
print(f"Você digitou {cont}, números.")
