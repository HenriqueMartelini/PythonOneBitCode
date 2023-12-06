gameName = "Fifa 23"
gameDescription = """
Fifa 23 e um jogo de futebol que e lancado anualmente uma versao do ano posterior.
Neste jogo voce pode jogar modo carreira, offline ou modo online.
"""
 
#string[inicio:fim] - indice comeca na posicao 0 / indice final - 1

# 1 - Busque toda string a partir da primeira posicao
print(gameName[0:])

# 2 - Busque toda string ate a ultima posicao
print(gameName[:7])

# 3 - Busuqe toda strung da terceira posicao ate a ultima
print(gameName[2:])


"""
string[inicio:fim:passo] - indice comeca na posicao 0 / indice final - 1
passo - determina o incrmente. Por padrao e 1
"""

# 4 - Busque toa a string de 2 em 2 caracteres
print(gameName[::2])

# 5 - Busque toda a string nos indices impares
print(gameName[1::2])

# 6 - Inverter uma string
print(gameName[::-1])