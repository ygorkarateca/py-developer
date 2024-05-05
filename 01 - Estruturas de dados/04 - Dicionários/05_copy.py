contatos = {
    "ygorbjj@gmail.com": {"nome": "ygor", "id": "2166"}   
}

copy = contatos.copy()
copy["ygorbjj@gmail.com"] = {"nome": "silva"}

contatos["ygorbjj@gmail.com"] # {"nome": "ygor", "id": "2166"}
copy["ygorbjj@gmail.com"] # {"nome": " Silva"}

print(copy)
print(contatos)