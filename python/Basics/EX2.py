"""
## Substituindo caractere repetido

Escreva um programa Python para obter uma string de uma determinada string em que todas as ocorrências de seu primeiro caractere foram alteradas para '$', exceto o próprio primeiro caractere

Ex:

fifa 23 → **fi#a 23**

restart→ resta#t

## Substituindo caractere repetido

Escreva um programa Python para obter uma única string de duas strings fornecidas,
separadas por um espaço e troque os dois primeiros caracteres de cada string.

Ex:

abc xyz → **xyc abz**
"""

name = input("Insira uma string: \n")

char = name[0].lower()
new = name.replace(char, "$")
new = char + new[1:]
print(new)

str1 = "abc"
str2 = "xyz"

new_str1 = str2[:2] + str1[2:]
new_str2 = str1[:2] + str2[2:]

print(f"Novas strings {new_str1} {new_str2}")