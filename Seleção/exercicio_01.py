# 1) Escreva um programa que leia o código de origem de um produto e imprima na tela a região de sua
# procedência conforme a tabela abaixo:
# código 1 Sul código 5 ou 6 Nordeste
# código 2 Norte código 7, 8 ou 9 Sudeste
# código 3 Leste código 10 Centro-Oeste
# código 4: Oeste código 11 Noroeste
# Observação: Caso o código não seja nenhum dos especificados o produto deve ser encarado como
# Importado.

cod = int(input("Qual é o codigo do produto? "))

if cod == 1:
    print("Este produto é da região Sul!")
elif cod == 2:
    print("Este produto é da região Norte!")
elif cod == 3:
    print("Este produto é da região Leste!")
elif cod == 4:
    print("Este produto é da região Oeste!")
elif cod == 2:
    print("Este produto é da região Norte!")
elif cod == 5 or cod == 6:
    print("Este produto é da região Nordeste!")
elif cod == 7 or cod == 8 or cod == 9:
    print("Este produto é da região Sudeste!")
elif cod == 10:
    print("Este produto é da região Centro-Oeste!")
elif cod == 11:
    print("Este produto é da região Noroeste!")
else:
    print("Este produto é Importado!")
