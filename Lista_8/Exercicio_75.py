# 75) Elabore um algoritmo que gere e escreve os números ímpares entre números entre 100 e 200.

par = []
impar = []

for i in range(100, 201):
    if i % 2 == 0:
        print(f"{i} é par")
        par.append(i)
    else:
        print(f"{i} é ímpar")
        impar.append(i)

print("\n\nNúmeros pares: ", par)
print("\nNúmeros ímpares: ", impar, "\n\n")
