# 3) Fazer um algoritmo para calcular a média de um aluno. São dados o número do aluno e suas três
# notas. No final, o algoritmo deverá escrever o número do aluno e sua média.

aluno = int(input("Qula o número de matricula do aluno: "))
nota = []
for i in range(1, 4):
    nota.append(float(input(f"Qual é {i}ª nota: ")))
    
soma = sum(nota)
media = soma/3
print(f"{aluno} teve uma media de {media:.2f}")