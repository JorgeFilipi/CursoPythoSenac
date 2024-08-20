# 21) Escreva um programa que leia as medidas dos lados de um triângulo e escreva se ele é
# Equilátero, Isósceles ou Escaleno. Sendo que:
# - Triângulo Equilátero: possui os 3 lados iguais
# - Triângulo Isósceles: possui 2 lados iguais.
# - Triângulo Escaleno: possui 3 lados diferentes.

m1 = float(input("Digite a 1ª medida: "))
m2 = float(input("Digite a 2ª medida: "))
m3 = float(input("Digite a 3ª medida: "))

if m1 == m2 and m2 == m3:
    print("Triângulo Equilátero!")
elif m1 == m2 and m2 != m3 or m2 == m3 and m1 != m2 or m1 == m3 and m2 != m3:
    print("Triângulo Isósceles")
else:
    print("Triângulo Escaleno")
