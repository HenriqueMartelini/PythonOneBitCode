name = input("Digite o nome do jogo:\n")
yearLaunch = int(input("Digite o ano de lancamento do jogo:\n"))
classification = float(input("Digite a nota de classificacao do jogo:\n"))

if  classification > 8.0:
    print(f"O jogo {name} e bem avaliado! Recomendado jogar.")
else:
    print(f"O jogo {name} ainda nao atingiu uma boa nota. Por isso nao recomendamos.")