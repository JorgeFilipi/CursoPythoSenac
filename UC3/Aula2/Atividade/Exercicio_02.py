# Exercício 2: Loop de Números Primos
#
# Objetivo: Escrever um script que identifique números primos em um intervalo.
#
# - Descrição: Use um loop ‘for’ para iterar de 2 até um número ( N ) fornecido pelo usuário e dentro do loop,
# use outro loop para verificar se o número atual é primo. Imprima cada número primo encontrado.


def encontrarPrimos(fim):
    print(f"Números primos até {fim}")
    for i in range(1, fim + 1):
        cont = 0
        for x in range(1, fim + 1):
            if i % x == 0:
                cont += 1
        if cont < 3:
            print(i)


fim = int(input("Digita um número: "))
encontrarPrimos(fim)

