import pprint

gamesDict = {
    "Escape From Tarkov": {
        "yearLaunch": 2017,
        "classification": 9.8,
        "genre": ["FPS", "survivor"]
    },
    "Star Wars Survivor":{
        "yearLaunch": 2019,
        "classification": 9.8,
        "genre": ["Adventure", "action"]
    },
    "Red Dead Redemption 2":{
        "yearLaunch": 2018,
        "classification": 9.8,
        "genre": ["Adventure", "action"]
    }
}

pp = pprint.PrettyPrinter(depth=4)
pp.pprint(gamesDict)

#1 - Buscar informação dentro de um dicionário alinhado
print(gamesDict["Escape From Tarkov"]["genre"])

#2 - Adicionar novo item
gamesDict["Escape From Tarkov"]["players"] = 1
print(gamesDict["Escape From Tarkov"])

#3 - Excluir um dicionário
del gamesDict["Red Dead Redemption 2"]
pp.pprint(gamesDict)