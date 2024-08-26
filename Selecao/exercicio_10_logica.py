# 10) Escreva um programa para ler 3 valores inteiros (considere que não serão lidos valores iguais) e
# escrevê-los em ordem crescente.

# solução com logica para varios números

def escreverLista():
    listaNumeros = []
    tamanho = int(input("Qual o tamanho da lista qie você quer escrever: "))
    tamanho += 1
    for i in range(1, tamanho):
        listaNumeros.append(float(input(f'Digite o {i}º valor: ')))
    return listaNumeros


def ordenaLista(lista):
    final = len(lista)
    while final > 0:
        i = 0
        while i < final - 1:
            if lista[i] > lista[i + 1]:
                lista[i], lista[i + 1] = lista[i + 1], lista[i]
            i += 1
        final -= 1
    return lista


print("\n\n", ordenaLista(escreverLista()))
