# Exercício 5: Programa de Mensagens com Loop Infinito
#
# Objetivo: Desenvolver um programa que permita ao usuário enviar mensagens repetidamente até decidir sair.
#
# - Descrição: Implemente um loop infinito que peça ao usuário para digitar uma mensagem. Após cada mensagem, pergunte se o usuário deseja continuar ou sair.
# Use a palavra-chave 'sair' para quebrar o loop. Cada mensagem, juntamente com uma confirmação de recebimento, deve ser exibida na tela.

while tuple:
    texto = input("Digite uma mensagem:\n")
    print(texto,"\n")
    resp = input("Digite 'S' para sair ou qualquer coisa para continuar: ").upper()
    if resp == 'S':
        break