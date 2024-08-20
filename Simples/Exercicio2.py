# Escreva um programa para ler uma temperatura em graus Fahrenheit, calcular e escrever o valor
# correspondente em graus Celsius. (C = (F-32) * 5 / 9)

tempF = float(input("Qual é a temperatura em Fahrenheit: "))
tempC = (tempF-32)*5/9
print("A temperatura informada em Celsius é ", tempC)
