contatos = {
    "ygorbjj@gmail.com": {"nome": "ygor", "id": "2166"},
}

# contatos["chave"] # KeyError

teste_01 = contatos.get("chave") # None
print(teste_01)

teste_02 = contatos.get("chave", {}) # {}
print(teste_02)

teste_03 = contatos.get("ygorbjj@gmail.com", {}) # ygorbjj@gmail.com": {"nome": "ygor", "id": "2166"}
print(teste_03)