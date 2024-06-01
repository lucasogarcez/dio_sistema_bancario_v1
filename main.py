limite = 500
LIMITE_SAQUES = 3
numero_de_saques = 1
saldo = 0
total_deposito = 0
total_saque = 0
menu = f"""##MENU## 
    1 - Depósito
    2 - Saque
    3 - Extrato
    4 - Sair
    Digite uma opção: """

while True:
    opcao = int(input(menu))
    
    if opcao == 1:
        print("Depositando\n")
        valor = float(input("R$: "))
        saldo += valor
        total_deposito += valor
    elif opcao == 2:
        print("Sacando\n")
        valor = float(input("R$: "))
        if numero_de_saques <= LIMITE_SAQUES:
            if saldo >= valor and valor <= 500:
                saldo -= valor
                total_saque += valor
                numero_de_saques += 1
            elif saldo >= valor and valor > 500:
                print("Valor limite de saque excedido")
            else:
                print("Saldo insuficiente")
        else:
            print("Limite de saques diários atingido")

    elif opcao == 3:

        print(f"""##EXTRATO##
        Total depositado: R${total_deposito:.2f}
        Total sacado: R${total_saque:.2f}
        Saldo atual: R${saldo:.2f}""")
    elif opcao == 4: 
        break
    else:
        print("Opção inválida")