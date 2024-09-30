import random

def obterMensagemAleatoria ():
    mensagens = [
        "Ola Mundo",
        "Python é uma linguagem de programação poderosa",
        "Vamos aprender a programar python!",
        "Python é uma linguagem de programação interpretada.",
        "Python é uma linguagem de programação de alto nível."
    ]

    return random.choice(mensagens)