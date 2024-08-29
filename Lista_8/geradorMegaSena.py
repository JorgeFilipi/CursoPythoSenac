import random

jogo = []


def aposta():
    jogo = []
    for i in range(1, 7):
        num = int(input(f"Digite o {i}º número: "))
        jogo.append(num)
    return sorted(jogo)


def volante():
    lista = []
    for i in range(1, 61):
        lista.append(i)
    return lista


def sortear():
    listaSort = random.sample(volante(), 6)
    return sorted(listaSort)


def acerto():
    global jogo
    jogo = aposta()
    resolta = sortear()
    acert = 0
    for i in jogo:
        for x in resolta:
            if i == x:
                acert += 1
    return acert


pont = acerto()

print("\n")
print(sortear())
print(jogo)
print("\n")
print(f"Você teve um total de {pont}, acertos")
