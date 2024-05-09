def salvar_carro(marca, modelo, ano, placa):
    # Salva carro no banco de dados...abs
    print(f"Carro inserido com sucesso!\n{marca} / {modelo} / {ano} / {placa}")

salvar_carro("Honda", "Civic", 2005, "KNO-OF84")
print()
salvar_carro(marca="Toyota", modelo="Corolla", ano=2005, placa="KNO-7F44")
print()
salvar_carro(**{"marca": "Fiat", "modelo": "Uno", "ano": 2000, "placa": "GTA-2P12"})