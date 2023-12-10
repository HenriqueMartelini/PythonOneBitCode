"""
## Cálculo da Distância

Escreva um programa que pergunte a distância que um passageiro deseja percorrer em km.
Calcule o preço da passagem, cobrando R$ 0,50 por km para viagens de até de 200 km, e R$
0,35 para viagens mais longas.

## Aumento salário funcionário

Escreva um programa que pergunte o salário do funcionário e calcule o valor do aumento. Para
salários superiores a R$ 1.250,00, calcule um aumento de 10%. Para os inferiores ou iguais, de
15%.
"""

#1
distance = float(input("Digite quantos kilometros tera sua viagem:\n"))

if distance <= 200:
    price = distance * 0.5
else:
    price = distance * 0.3

print(f"O valor total de sua viagem ficara em {price}")

#2
salary = float(input("Digite o salario do funcionario:\n"))

perc_increase = 0.15

if salary > 1250:
    perc_increase = 0.1
increase = salary * perc_increase

print(f"Seu aumento sera de {increase:.2f}")



"""if salary > 1250:
    increase = salary * 0.1
    newSalary = salary + increase
    print(f"O funcionario recebera um aumento de {increase}, que representa 10% de seu atual salario, portanto seu novo salario sera de {newSalary}")
else:
    increase = salary * 0.15
    newSalary = salary + increase
    print(f"O funcionario recebera um aumento de {increase}, que representa 15% de seu atual salario, portanto seu novo salario sera de {newSalary}")"""