# 16) Acrescente as seguintes mensagens à solução do exercício anterior conforme o caso.
# - Caso o número de lados seja inferior a 3 escrever NÃO É UM POLÍGONO.
# - Caso o número de lados seja superior a 5 escrever POLÍGONO NÃO IDENTIFICADO.
# Observação: Considere que o usuário poderá informar qualquer valor para o número de lados.

lado = int(input("Qual o número de lados do poligono? "))
if lado == 3 or lado == 4:
    medida = float(input("Qual é a medida da linha? "))

if lado < 3:
    print("NÃO É UM POLÍGONO")
elif lado == 3:
    peri = medida * 3
    print("TRIÂNGULO o perímetro é ", peri)
elif lado == 4:
    area = lado ** 2
    print("QUADRADO e a sua área é", area)
elif lado == 5:
    print("PENTÁGONO")
else:
    print("POLÍGONO NÃO IDENTIFICADO")
