# 76) Construa um algoritmo que leia 50 valores inteiros e positivos e:
# · Encontre o maior valor
# · Encontre o menor valor
# · Calcule a média dos números lidos

# OBS1.: Refaça o exercicio usando lista para armazenar valores digitados pelo usuario.
# OBS2.: Façao com que o sistema sorteie 6 valores digitados pelo usuario logo após o exibir as mensagens


import random

maior = 0
menor = 1000
total = 0
lista = []

for i in range(1, 11):
    valorTemp = int(input(f"Qaul o {i}º valor: "))
    lista.append(valorTemp)
    total += valorTemp
    if valorTemp > maior:
        maior = valorTemp
    if valorTemp < menor:
        menor = valorTemp

media = total / 5

lista2 = random.sample(lista, 5)

print(f"\n\nMedia: {media:.2f}")
print(f"Total {total}")
print(f"Maior {maior}")
print(f"Menor {menor}\n")
print(lista)
print(lista2)
