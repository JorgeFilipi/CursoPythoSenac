# 23) Escreva um programa que leia o valor de 3 ângulos de um triângulo e escreva se o triângulo é
# Acutângulo, Retângulo ou Obtusângulo. Sendo que:
# - Triângulo Retângulo: possui um ângulo reto. (igual a 90°)
# - Triângulo Obtusângulo: possui um ângulo obtuso. (maior que 90°)
# - Triângulo Acutângulo: possui três ângulos agudos. (menor que 90°)

a1 = float(input("Digite o 1º ângulo: "))
a2 = float(input("Digite o 2º ângulo: "))
a3 = float(input("Digite o 2º ângulo: "))

if a1 == 90 or a2 == 90 or a3 == 90:
    print("Triângulo Retângulo")
elif a1 > 90 or a2 > 90 or a3 > 90:
    print("Triângulo Obtusângulo")
elif a1 < 90 and a2 < 90 and a3 < 90:
    print("Triângulo Acutângulo")
