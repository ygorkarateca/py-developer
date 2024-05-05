contatos = {
    "ygorbjj@gmail.com": {"nome":"ygor", "id": "2166"},
}

teste_01 = contatos.popitem() # ("ygorbjj@gmail.com": {"nome":"ygor", "id": "2166"})
teste_02 = contatos.popitem() # KeyError

print(teste_01)