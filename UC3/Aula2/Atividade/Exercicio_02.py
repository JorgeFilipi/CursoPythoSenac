# Exercício 2: Loop de Números Primos
#
# Objetivo: Escrever um script que identifique números primos em um intervalo.
#
# - Descrição: Use um loop ‘for’ para iterar de 2 até um número ( N ) fornecido pelo usuário e dentro do loop,
# use outro loop para verificar se o número atual é primo. Imprima cada número primo encontrado.


def encontrarPrimos(fim):
    primos = []
    for num in range(fim + 1):
        if num > 0:
            for i in range(2, int(num ** 0.5) + 1):
                if (num % i) == 0:
                    break
            else:
                primos.append(num)
    return primos


fim = int(input("Digita um número: "))
print(f"Números primos até {fim}: {encontrarPrimos(fim)}")

