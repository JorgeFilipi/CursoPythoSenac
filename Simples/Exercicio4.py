# Escreva um programa para calcular e imprimir o número de lâmpadas necessárias para iluminar um
# determinado cômodo de uma residência. Dados de entrada: a potência da lâmpada utilizada (em watts),
# as dimensões (largura e comprimento, em metros) do cômodo. Considere que a potência necessária é
# de 18 watts por metro quadrado.

larg = float(input("Informe a lagura do comudo: "))
comp = float(input("Informe o comprimento do comudo: "))
watts = (larg*comp)*18
print("Para iluminar este comudo sãp necessario", watts, "Watts de potência")
