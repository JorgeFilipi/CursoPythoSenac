# A equipe Benneton-Ford deseja calcular o número mínimo de litros que deverá colocar no tanque de
# seu carro para que ele possa percorrer um determinado número de voltas até o primeiro
# reabastecimento. Escreva um programa que leia o comprimento da pista (em metros), o número total de
# voltas a serem percorridas no grande prêmio, o número de abastecimentos desejados e o consumo de
# combustível do carro (em Km/L). Calcular e escrever o número mínimo de litros necessários para
# percorrer até o primeiro reabastecimento. OBS: Considere que o número de voltas entre os
# abastecimentos é o mesmo.

tamanho_pista = 320
numero_voltas = 180
abastecimentos = 2
consulmo = 0.5
km_l = consulmo*1000/tamanho_pista
litros = km_l * (numero_voltas / abastecimentos)
volta_abastece = numero_voltas / abastecimentos

print(litros)
print(volta_abastece)
