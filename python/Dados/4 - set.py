gameSet = {"Fifa", "Mario", "RDR2", "Zelda", "Resident Evil", "Satr Wars", True, 1, 90.50}
print(gameSet)

#1 - Buscar o tamanho do set
print(len(gameSet))

#2 - True e 1 são considerados o mesmo valor
exampleSet = {"Fifa", True, 1, 90.50}
print(exampleSet)

#3 - Adicionar item de outro set
exampleSet.update(exampleSet)
print(gameSet)

#4 - Remvoer itens do set
gameSet.remove(True)
gameSet.remove(90.50)
print(gameSet)


#Não possibilita recuperar valores via fatiamento ou slice