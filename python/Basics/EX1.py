"""
Antecessor e Sucessor de um número
Escreva um programa em Python que leia um número e represente o número antecessor e sucessor desse 
número que foi lido, utilizando operadores de atribuição.


Média de 4 notas
Escreva um programa em Python que leia quatro números e calcule a média entre esses números
"""

num = int(input("Insira um numero:\n"))

print(f"O numero {num} possui antecessor de valor {num - 1} e sucessor de valor {num + 1}")

num1 = float(input("Insira a pirmeira nota:\n"))
num2 = float(input("Insira a segunda nota:\n"))
num3 = float(input("Insira a terceira nota:\n"))
num4 = float(input("Insira a quarta nota:\n"))

average = (num1 + num2 + num3 + num4) / 4

print(f"A media das notas {num1} {num2} {num3} {num4} e {average}")