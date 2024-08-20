# 7) Escreva um programa para ler 2 valores (considere que não serão informados valores iguais) e
# escrever o maior deles.

nu1 = int(input("Escreva um número: "))
nu2 = int(input("Escreva outro número: "))

if nu1 > nu2:
    print(nu1, "É o maiso número entre os dois!")
elif nu2 > nu1:
    print(nu2, "É o maiso número entre os dois!")
else:
    print("Os dois números são iguais", nu1, "e", nu2)
