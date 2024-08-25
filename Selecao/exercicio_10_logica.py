# 10) Escreva um programa para ler 3 valores inteiros (considere que não serão lidos valores iguais) e
# escrevê-los em ordem crescente.

# solução com logica para varios números

# list = [5, 4, 3, 2, 1]


def escreverLista():
    listaNumeros = []
    tamanho = int(input("Qual o tamanho da lista qie você quer escrever: "))
    tamanho += 1
    for i in range(1, tamanho):
        listaNumeros.append(int(input(f'Digite o {i}º valor: ')))
    return listaNumeros


def ordenaLista(v):
    fim = len(v)
    while fim > 0:
        i = 0
        while i < fim - 1:
            if v[i] > v[i + 1]:
                v[i], v[i + 1] = v[i + 1], v[i]
            i += 1
        fim -= 1
    return v


print("\n\n", ordenaLista(escreverLista()))
