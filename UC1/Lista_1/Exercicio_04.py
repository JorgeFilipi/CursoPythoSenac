# 4) O diretor industrial de uma companhia, solicitou ao responsável do setor de informática, o salário do
# funcionário A. são fornecidos os seguintes dados: o nome do funcionário, o número de horas trabalhadas
# e o valor que ele recebe por hora. Calcular o salário deste funcionário. No final o algoritmo deverá
# escrever o nome do funcionário e o seu salário.

nome = str(input("Qual o nome do funcionário: ").title())
horaT = int(input("QUantas horas ele trabalhou: "))
VHORAS = 45.90 

salario = horaT * VHORAS

print(f"O funcionário {nome}, deve receber R${salario:.2f}")