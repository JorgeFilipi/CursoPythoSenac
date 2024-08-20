# 15) Escreva um programa para ler o número de lados de um polígono regular e a medida do lado (em
# cm). Calcular e imprimir o seguinte:
# - Se o número de lados for igual a 3 escrever TRIÂNGULO e o valor do seu perímetro.
# - Se o número de lados for igual a 4 escrever QUADRADO e o valor da sua área.
# - Se o número de lados for igual a 5 escrever PENTÁGONO.
# Observação: Considere que o usuário só informará os valores 3, 4 ou 5

lado = int(input("Qual o número de lados do poligono? "))
if lado == 3 or lado == 4:
    medida = float(input("Qual é a medida da linha? "))

if lado == 3:
    peri = medida * 3
    print("TRIÂNGULO o perímetro é ", peri)
elif lado == 4:
    area = lado ** 2
    print("QUADRADO e a sua área é", area)
elif lado == 5:
    print("PENTÁGONO")
