import  mensagens

def solicitarMensagens (nome):
    return f"Olá {nome}!\nMensagem: {mensagens.obterMensagemAleatoria()}"


def main():
    print("\n### Bem-vindo  ao programa aula 03. ###")
    nome = input("Qual é o seu nome: ").title()
    mensagens = solicitarMensagens(nome)
    print("\n", mensagens)
    print("\n### Fim do programa.###")

if __name__ == "__main__":
    main()