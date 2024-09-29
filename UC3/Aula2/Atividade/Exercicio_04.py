# Exercício 4: Simulador de Dados Financeiros
#
# Objetivo: Simular o saldo de uma conta com juros compostos usando loops e incrementadores.
#
# - Descrição: Solicite ao usuário um saldo inicial, a taxa de juros anual e o número de anos. Use um loop ‘while’
# para simular o aumento do saldo com juros compostos ao longo dos anos e imprima o saldo final após o período especificado.

saldo = float(input("Digite o saldo inicial da conta: R$").replace(',','.'))
juros = float(input("Digite a taxa de juros anual: ").replace(',','.'))
anos = int(input("Digite a quantidade de anos para calcular o saldo: "))
i = 0

while i < anos:
    i += 1
    saldo = saldo * juros + saldo


print(f"O saldo final da conta é R${saldo:.2f}")

