# 8) Escreva um programa para ler o ano de nascimento de uma pessoa e escrever uma mensagem que
# diga se ela poderá ou não votar este ano (não é necessário considerar o mês em que ela nasceu).

ano = int(input("Qual o ano que você nasceu com quatro digitos XXXX: "))

if ano > 2009:
    print("Você ainda não pode votar este ano!")
else:
    print("Você já pode votar este ano!")
