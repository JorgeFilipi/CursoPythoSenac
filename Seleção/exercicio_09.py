# 9) As maçãs custam R$ 0,30 cada se forem compradas menos do que uma dúzia, e R$ 0,25 se forem
# compradas pelo menos doze. Escreva um programa que leia o número de maçãs compradas, calcule e
# escreva o valor total da compra.

proco = 0
quant = int(input("Quantas maçã você vai querer? "))

if quant >= 12:
    proco = quant * 0.25
    print(f"Sua compra deu R${proco:,.2f}")
else:
    proco = quant * 0.30
    print(f"Sua compra deu R${proco:,.2f}")
