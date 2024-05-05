contatos = {
    "ygorbjj@gmail.com": {"nome": "ygor", "id": "2166"},
    "ygorbjj20@gmail.com": {"nome": "Fernandes", "id": "8800"},
    "ygorbjj@live.com": {"nome": "Silva", "id": "1090"},
    "ygorkarateca@outlook.com": {"nome": "Santos", "id":"2142"},
}

for chave in contatos:
    print(chave, contatos[chave])

print("=" * 67)

for chave, valor in contatos.items():
    print(chave, valor)