valor = float(input())

saldo_em_conta=0
def soma_valor(p):
    if p == 0:
        print("Encerrando o programa. Obrigado!")
    elif p < 0:
        print("Valor inválido. Digite um valor maior que zero..")
    else:
        global saldo_em_conta
        saldo_em_conta += p
        print(f"Depósito realizado com sucesso!\nSaldo atual: R${saldo_em_conta:.2f}")



soma_valor(valor)



# else > 0:
# # TODO: Imprimir a mensagem de sucesso, formatando o saldo atual (vide Exemplos).
# print(f"Depósito realizado com sucesso! Novo saldo: R${valor:.2f}")
# elif valor == 0:
# # TODO: Imprimir a mensagem de valor inválido.
# print("Valor inválido. Digite um valor maior que zero..")
# if
#     # TODO: Imprimir a mensagem de encerrar o programa.
#     print("Encerrando o programa. Obrigado!")

