"""
    TUPLAS -> Tuplas são imutaveis, mas é possivel sobrescrever os seus valores
    por quê utilizar tuplas?
    tuplas são mais rapidas do que listas
    otimo para trabalhar com data science e big data
    tuplas deixam o seu codigo mais seguro, por conta da imutabilidade
"""

# Criando dados para manipulacao
tupla1 = (1, 2, 3, 4)
tupla2 = (5, 6, 7, 8)

# Somando os valores da tupla
print(sum(tupla1))

# Exibindo o maior valor da tupla
print(max(tupla1))

# Exibindo o menor valor da tupla
print(min(tupla1))

# Exibindo a quantidade de elementos dentro da tupla
print(len(tupla1))

# Concatenando as tuplas em uma nova tupla
tupla3 = tupla1 + tupla2


print(tupla1.count(2))
print(tupla2)
print(tupla3)

# Imprimindo os valores usando slice
print(tupla3[2:4])

# Imprimindo os valores da tupla
for value in tupla3:
    print(value)

# Usando o index para saber a posicao do elemento na lista ou na tupla
position = tupla3.index(5)
print(position)

print(dir(tupla3))
