# 22) Escreva um programa que leia a idade de 2 homens e 2 mulheres (considere que a idade dos
# homens será sempre diferente, assim como das mulheres). Calcule e escreva a soma das idades do
# homem mais velho com a mulher mais nova, e o produto das idades do homem mais novo com a
# mulher mais velha.

idadeH1 = int(input("Qual é a idade do 1º homem: "))
idadeH2 = int(input("Qual é a idade do 2º homem: "))
idadeM1 = int(input("Qual é a idade da 1ª mulher: "))
idadeM2 = int(input("Qual é a idade da 2º mulher: "))

hMaior = 0
hMenor = 0
mMaior = 0
mMenor = 0

if idadeH1 > idadeH2:
    hMaior = idadeH1
    hMenor = idadeH2
else:
    hMaior = idadeH2
    hMenor = idadeH1

if idadeM1 > idadeM2:
    mMaior = idadeM1
    mMenor = idadeM2
else:
    mMaior = idadeM2
    mMenor = idadeM1

print(hMaior + hMenor)
print(hMenor * mMaior)
