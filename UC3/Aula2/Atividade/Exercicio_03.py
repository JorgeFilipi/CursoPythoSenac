# Exercício 3: Controle de Formatação de Números Decimais
#
# Objetivo: Criar um programa que formate números decimais.
#
# - Descrição: Peça ao usuário para inserir um número flutuante e o número de casas decimais desejado.
# Use f-strings para formatar o número com o número de casas decimais especificado e exiba o resultado.

num = float(input("Digite um numero decimal: ").replace(',','.'))
print(f"O número ditado é {num:.2f}")