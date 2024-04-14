# pares.append(numeros)

convidados = ["Ygor", "Daniel", "Miguel", "Paulinho"]
convidados_futuros = ""

opcao = int(input("Digite:\n[1]ADICIONAR\n[2]REMOVER\n[3]SAIR\n"))

while True:

    # Adicionar nomes
    if opcao == "1":

        adicionar_convidados = str(input()).title()
        print(f"Digite o nome para adicionar:{adicionar_convidados.append()}")

    # Remover nomes
    elif opcao == "2":
        convidados.remove()

    # Mostrar nomes atuais
    elif opcao == "3":
        print(convidados)

    # Sair
    else:
        break