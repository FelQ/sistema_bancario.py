menu = '''

[d] Depositar:

[s] Sacar:

[e] Extrato:

[q] sair:

==> '''

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)
    if opcao == "d":
        valor = float(input("Digite o valor a ser creditado em sua conta: "))
        if valor > 0:
            saldo += valor
            extrato += (f"Depósito: R$ {valor:.2f}\n")
        
        else:
            print("Operação inválida. Informe um valor inteiro e positivo!")
    
    elif opcao == "s":
        valor = float(input("Digite o valor que deseja sacar: "))
        if valor <= saldo and valor <= 500 and numero_saques < LIMITE_SAQUES:
            numero_saques += 1
            saldo -= valor
            extrato += (f"Saque: R$ {valor:.2f}\n")
        
        else:
            print("Operação não permitida!")
    
    elif opcao == "e":
       print("\n================ EXTRATO ================")
       print("Não foram realizadas movimentações." if not extrato else extrato)
       print(f"\nSaldo: R$ {saldo:.2f}")
       print("==========================================")
       
    elif opcao == "q":
        print("Encerrando o programa!")
        break
    
    else:
        print("Opção inválida! Por favor selecione a opção desejada.")