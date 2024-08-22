# 4) Acrescente ao exercício anterior a mensagem Você foi REPROVADO! Estude mais... caso a
# média calculada seja menor que 6.0.

n1 = float(input("Qual é a mota da P1: "))
n2 = float(input("Qual é a mota da P2: "))

media = (n1 + n2)/2

if media >= 6:
    print("PARABÉNS!")
else:
    print("REPROVADO! Estude mais...")
