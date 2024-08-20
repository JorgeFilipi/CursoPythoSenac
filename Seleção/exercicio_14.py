# 14) Escreva um programa para ler o número de gols marcados pelo Grêmio e o número de gols
# marcados pelo Inter em um GRENAL. Escrever o nome do vencedor. Caso não haja vencedor deverá
# ser impressa a palavra EMPATE.

gremio = int(input("Qual o número de gol dos Grêmio? "))
inter = int(input("Qual o número de gol do Inter? "))

if gremio > inter:
    print("O Grêmio é o vencedor!")
elif inter > gremio:
    print("O Inter é o vencedor!")
else:
    print("Não teve vencedor ouve um EMPATE!")
