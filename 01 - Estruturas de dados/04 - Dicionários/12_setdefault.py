contato = {"nome": "silva", "id": "2166"}

teste_01 = contato.setdefault("nome", "giovanna")
print(teste_01)

teste_02 = contato.setdefault("idade", 28)
print(teste_02)
print(contato)