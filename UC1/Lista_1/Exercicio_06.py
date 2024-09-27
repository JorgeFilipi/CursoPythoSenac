# 6) Num dispositivo de entrada de dados, estão disponíveis as informações de um vendedor conforme
# abaixo:
# • Nome do vendedor.
# • Salário fixo.
# • Total de vendas por ele efetuadas.
# • Percentual que ele recebe sobre o total de vendas.
from numpy.core.defchararray import title

# Elaborar um algoritmo para ler os dados anteriores e calcular o salário total do vendedor. No final,
# escrever o nome do vendedor e o seu salário total.

nome = str(input("Qual o nome do vendedor? ").title())
salario = float(input("Qual o salario base do vendedor? "))
venda = float(input("Qual o total de vendas deste vendador: "))
perce = float(input("Qual o percentual de vendas deste vendedor: "))

salarioTotal = salario + venda * perce

print(f"O vendedor {nome}, deve receber R${salarioTotal}")