"""
 Mapas -> conhecidos em python como dicionarios

 Dicionarios em python são representados por chaves {}

 interar sobre dicionarios

 for chave in receita:
    print(receita[chave])
"""

receita = dict(jan=12, fev=15, mar=43)

# Imprimindo os valores das chaves
for chave in receita.keys():
    print(receita[chave])

# Acessando os valores
print(receita.values())

for valor in receita.values():
    print(valor)

# Imprimindo itens do dicionario
print(receita.items())

# Imprimindo chave e valor com items()
for chave, value in receita.items():
    print(f"mês: {chave} e valor:  {value}")

# somando valores do dicionario
print("O valor somado é:", sum(receita.values()))

# pegando o valor minimo do dicionario
print("O valor minimo é:", min(receita.values()))

# Pegando o valor maximo do dicionario
print("O valor maximo é:", max(receita.values()))
