def criar_carro(modelo, ano, placa, /, marca, motor, combustivel):
    print(modelo, ano, marca, motor, combustivel)

criar_carro("Civic", 2005, "KNO-0F84", marca="Honda", motor="1.7", combustivel="Gasolina") # Metodo Válido
criar_carro(modelo="Civic", ano=2005, placa="KNO-0F84", marca="Honda", motor="1.7", combustivel="Gasolina") # Metodo Inválido