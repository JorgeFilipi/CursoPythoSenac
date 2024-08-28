# 74) Faça um algoritmo que conte de 1 a 100 e a cada múltiplo de 10 emita uma mensagem:
# “Múltiplo de 10”.

mult = int(input("Qual o intervalo de multiplos você quer saltar: "))
vFinal = int(input("Qual o valor final?"))
vInicial = int(input("Digite o valor inicial: "))

if vInicial < vFinal:
    for i in range(vInicial, vFinal+1):
        if (i % mult == 0):
            print(i, "multiplos de ", mult)
        else:
            print(i)
else:
    print("Não é posivel testar esse seguencia númerica!")
