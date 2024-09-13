# Escreva um programa para ler o raio de um círculo, calcular e escrever a sua área (Pi * (raio * raio))

import math

raio = float(input("Qual o valor do raio: "))


def areaCirculo(valorRaio):

    PI = math.pi
    area = PI*(valorRaio * valorRaio)
    return area


print(f"A área do circulo é {areaCirculo(raio):,.2f}")
