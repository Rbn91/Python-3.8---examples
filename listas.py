"""
    LISTAS-> Lista em python funciona como vetores/arrays de outras linguagens
    com a diferenca de serem dinamicas, podendo ser formadas com quaisquer tipos
    de dados.
"""

# criando uma lista
list_range = []
list_nome = []
list_random = [1, 4, 3, 5, 4, 3, 6, 8, 2, 32, 24, 5]

# Populando uma lista
list_range = list(range(0, 12, 2))

# Populando uma lista com um nome
list_nome = list("Robson Rodrigues de Souza")

print(list_nome)

# Usando o metodo sort para ordenar a lista
list_random.sort()

# Contando uma quantidade de caractere em uma lista

print(list_nome.count('o'))

print(list_random)

print(list_range)

# Adicionando informações em uma lista usando apend
list_random.append(7)
list_random.append([3, 2, 5])  # Adicionando dado em forma de lista como elemento unico
print(list_random)

# Adicionando uma serie de dados em uma lista usando extend
# Extend não aceita passar um valor unico, tem que ser mais de um valor ou dado iteravel
list_random.extend([43, 53, 356, 3, 32, 33, 235, 53])
print(list_random)

# Usando o Insert para adicionar um valor em uma determinada dosicao da lista
list_random.insert(4, 666)
print(list_random)

# Imprimindo a lista de valores reversa
list_random.reverse()
print(list_random)

# imprimindo a lista usando slice
print(list_nome[::-1])

# Criando uma copia da lista
new_name = list_nome.copy()
print(new_name)

# contato as strings de uma lista
print(len(list_random))

# removendo elementos de uma lista pelo indice
print(list_random)
list_random.pop()
print(list_random)

# Usando o clear para limpar os dados de uma lista criada
new_random = list_random.copy()
new_random.clear()
print(new_random)

# Usando split para criar uma lista de informações
# por padrao, o split separa a variavel nos espacos encontraodos.
texto = "Robson morava no mascarenhas e passou a morar no morumbi."
print(texto.split())


# Usando o join para concatenar caracteres na lista formando uma string com o resultado final
lista_palavra = ["maria", "carro", "sol", "azul"]

new_string = ' '.join(lista_palavra)
print(new_string)

new_string1 = '-'.join(lista_palavra)
print(new_string1)
