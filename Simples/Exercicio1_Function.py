# Escreva um programa para ler o raio de um círculo, calcular e escrever a sua área (Pi * (raio * raio))

import math

r = float(input("Qual o valor do raio: "))


def areaCirculo():

    PI = math.pi
    area = PI*(r*r)
    return area


print(f"A área do circulo é {areaCirculo():,.2f}")
