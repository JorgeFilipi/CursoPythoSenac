# 1) Para que a divisão entre 2 números possa ser realizada, o divisor não pode ser nulo (zero). Escreva
# um programa para ler 2 valores e imprimir o resultado da divisão do primeiro pelo segundo. OBS: 0
# programa deve validar a leitura do segundo valor (que não deve ser nulo). Enquanto for fornecido um
# valor nulo a leitura deve ser repetida. Utilize a estrutura Repita/Até na construção da repetição de
# validação

n1 = float(input("Escreva um número: "))
cond = True

while cond:
    n2 = float(input("Escreva outro número diferente de zero: "))
    if n2 != 0:
        cond = False

print(n1 / n2)
