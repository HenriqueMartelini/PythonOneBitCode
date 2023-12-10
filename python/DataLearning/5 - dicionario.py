gameTarkov = {
    "name": "Tarkov",
    "yearLaunch": 2017,
    "gamePrice": 50,
    "classification": 9.8,
    "genre": ["fps", "survivor"]
}
print(gameTarkov)
print(len(gameTarkov))
print(type(gameTarkov))

#1 - Recuperar elemento do dicionário
print(gameTarkov['genre'])
print(gameTarkov.get('classification'))

#2 - Recuperar as chaves do dicionário
print(gameTarkov.keys())

#3 - Buscar apenas os valores do dicionário
print(gameTarkov.values())

#4 - Buscar itens do dicionário com chave e valor
print(gameTarkov.items())

#5 - Adicionar itens ao dicionário
gameTarkov["players"] = 1;
print(gameTarkov)

#6 - Atualizar dados do dicionário
gameTarkov.update({"players": 1})
print(gameTarkov)

#7 - Remover item do dicionário
gameTarkov.pop("players")
print(gameTarkov)