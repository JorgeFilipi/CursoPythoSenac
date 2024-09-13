# 50) Elaborar um algoritmo em pseudocodigo que efetue a leitura do nome e do sexo de uma
# pessoa, apresentando como saída uma das seguintes mensagens: “Ilmo Sr.”, para o sexo
# informado como masculino, ou a mensagem “Ilma Sra.”, para o sexo informado como feminino.
# Apresente na seqüência da mensagem impressa o nome da pessoa.

nome = str(input("Digite o seu nome: ").title())
sexo = str(input("Qual o seu sexo(M ou H)").lower())

if sexo == "m":
    print("Olá Ilma Sra.", nome)
else:
    print("Olá Ilmo Sr.", nome)
