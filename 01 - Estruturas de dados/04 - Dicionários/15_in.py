contatos = {
    "ygorbjj@gmail.com": {"nome": "ygor", "id": "2166"},
    "ygorbjj20@gmail.com": {"nome": "Fernandes", "id": "8800"},
    "ygorbjj@live.com": {"nome": "Silva", "id": "1090"},
    "ygorkarateca@outlook.com": {"nome": "Santos", "id":"2142"},
}

teste_01 = "ygorkarateca@gmail.com" in contatos
print(teste_01) # False

teste_02 = "ygorbjj@gmail.com" in contatos
print(teste_02) # True

teste_03 = "id" in contatos["ygorbjj@gmail.com"]
print(teste_03) # True

teste_04 = "idade" in contatos["ygorbjj20@gmail.com"]
print(teste_04) # False