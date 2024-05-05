contatos = {
    "ygorbjj@gmail.com": {"nome": "ygor", "id": "2166"},

}

teste_01 = contatos.fromkeys(["nome", "id"]) # {"nome": None, "id": None}
teste_02 = contatos.fromkeys(["nome", "id"], "vazio") # {"nome": vazio, "id": vazio}

print(contatos, teste_02)