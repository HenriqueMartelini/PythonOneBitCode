gameList = ["Fifa", "Resident Evil", "Red Dead Redemption",
            "Star Wars Fallen Order", "The legend of Zelda"]

# 1 - Tamanho da lista
print(len(gameList))

#2 - Recuperar um item da lista peli índice
print(gameList.index("Red Dead Redemption"))

#3 - Adicionar item ao final da lista
gameList.append("GTA V")
print(gameList)

#4 - Ordenar a lista
gameList.sort()
print(gameList)

#5 - Copiar os itens de uma lista para outra
gameReset = gameList.copy()
gameReset.remove("The legend of Zelda")
print(gameReset)

#6 - Remove todos os itens de uma lista
gameList.clear()
print(gameList)
print(gameReset)