# Ummotorista de táxi deseja calcular o rendimento de seu carro na praça. Sabendo-se que o preço do
# combustível é de R$ 4,87, escreva um programa para ler: a marcação do odômetro (Km) no início do
# dia, a marcação (Km) no final do dia, o número de litros de combustível gasto e o valor total (R$)
# recebido dos passageiros. Calcular e escrever: a média do consumo em Km/L e o lucro (líquido) do dia.

km_inicio = int(input('Qual o KM inicial do dia: '))
km_final = int(input('Qual o KM no fianl do dia: '))
caixa = float(
    input('Qual foi o valor total acumulado duratnet o dia de trabalho: '))
abast = int(input('Quantos litros foi abastecido durante o dia: '))
gaso = 4.78
roda = km_final-km_inicio
gasto = gaso*abast
lucro = caixa-gasto

print('o taxi rodou', roda, 'gastou com gasolina',
      gasto, 'e teve um lucro de', lucro)
