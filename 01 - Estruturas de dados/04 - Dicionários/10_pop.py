contatos = {
    "ygorbjj@gmail.com": {"nome": "ygor", "id": "2166"},

}

teste_01 = contatos.pop("ygorbjj@gmail.com") # Remove a chave do dicionario
teste_02 = contatos.pop("ygorbjj@gmail.com", "Chave não encontrada")

print(teste_01, teste_02)