# 17) Escreva um programa para ler 2 valores inteiros e uma das seguintes operações a serem
# executadas (codificada da seguinte forma: 1. Adição, 2.Subtração, 3.Divisão, 4.Multiplicação). Calcular e
# escrever o resultado dessa operação sobre os dois valores lidos. Observação: Considere que só serão
# lidos os valores 1, 2, 3 ou 4.

valor1 = int(input("Escreva um valor: "))
valor2 = int(input("Escreva um valor: "))
total = 0
opcao = int(
    input("1 SOMA\n2 SUBTRAÇÂO\n3 DIVISÂO\n4 MULTIPLICAÇÂO\nQual opção você quer: "))

if opcao == 1:
    total = valor1 + valor2
    print(total)
elif opcao == 2:
    total = valor1 - valor2
    print(total)
elif opcao == 3:
    total = valor1 / valor2
    print(total)
elif opcao == 4:
    total = valor1 * valor2
    print(total)
