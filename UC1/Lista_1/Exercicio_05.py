# 5) Fazer um algoritmo que lê cinco valores inteiros e positivos. Calcular a média aritmética e a média
# harmônica. Escrever os valores lidos e as duas médias calculadas.
# Para calcular as médias temos as seguintes fórmulas:
# media aritmética (a+b+c+d+e)/5
# media harmônica 5/((1/a)+(1/b)+(1/c)+(1/d)+(1/d))

print("Vamos calcular a media de 5 números\n")
numA = float(input("Digete o 1º número: "))
numB = float(input("Digete o 2º número: "))
numC = float(input("Digete o 3º número: "))
numD = float(input("Digete o 4º número: "))
numE = float(input("Digete o 5º número: "))

mediaA = (numA + numB + numC + numD + numE) / 5
mediaH = 5 / ((1 / numA) + (1 / numB) + (1 / numC) + (1 / numD) + (1 / numE))

print(f"A media aritimética é {mediaA:.2f}, a media harmônica é {mediaH:.2f}")