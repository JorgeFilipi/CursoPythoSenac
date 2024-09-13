# 8) Escreva um programa para ler o ano de nascimento de uma pessoa e escrever uma mensagem que
# diga se ela poderá ou não votar este ano (não é necessário considerar o mês em que ela nasceu).

from datetime import date as dt

anoNasci = int(input("Qual o ano que você nasceu com quatro digitos XXXX: "))


def verificarVotoIdade(idadeUser):

    if idadeUser < 16:
        return "Você ainda não pode votar este ano!"
    else:
        return "Você já pode votar este ano!"


def idade(nascimento):
    anoAtu = dt.today().year
    return anoAtu - nascimento


idadeAtualUser = idade(anoNasci)

print(verificarVotoIdade(idadeAtualUser))
print("Sua idade atual é", idadeAtualUser, "anos")
