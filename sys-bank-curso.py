menu = """"

[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saque = 0
LIMITE_SAQUE = 3

while True:

    opcao = input(menu)

    if opcao == "1":
        print("Depósito")
    
    elif opcao == "2":
        print("Saque")

    elif opcao == "3":
        print("Extrato")

    elif opcao == "4":
        break

    else:
        print("Operacão Inválida, Por favor selecione novamente a operacao desejada.")