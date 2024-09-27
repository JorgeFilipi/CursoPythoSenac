# 2. Questão 2: Condições Compostas
#    - Enunciado: Pergunte ao usuário dois valores:
# sua idade e se ele possui permissão dos pais (sim/não).
# Se o usuário tiver menos de 18 anos e não tiver permissão dos pais,
# ele não pode participar da viagem. Use operadores lógicos para avaliar as condições.
# Código Inicial:
# idade = int(input("Digite sua idade: "))
# permissao = input("Você tem permissão dos pais? (sim/não): ")

idade = int(input("Digite sua idade: "))
permissao = str(input("Você tem permissão dos pais? (sim/não): ").upper())

if idade > 17:
    if permissao == "S":
        print("Você pode participar da viagem!")
    else:
        print("Você não pode ir na viagem!")
else:
    print("Você é menor de idade não pode ir na viagem!")