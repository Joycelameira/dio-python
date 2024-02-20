opção = -1
while opção != 0:
    opção = int(input("[1] Sacar \n [2] Extrato \n [0] Sair \n:"))

    if opção == 1:
        print("Sacando...")
    elif opção == 2:
        print("Exibindo o extrato...")

else:
    print("Obrigado por usar nosso sistema bancário, até logo!")
