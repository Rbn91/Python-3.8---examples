"""
Conjuntos de dados no python usando set
set - Não pode ter conjuntos de dados repetidos, pois ele ignora e não printa elementos repetipos
"""

# Construindo um set de valores repetidos e imprimindo.
s = set({1, 2, 3, 4, 5, 4, 5, 6, 54, 6, 7, 65, 5, 6})

# Exibe os valores mas não os seus dados repetidos
print(s)

# Imprimindo os valores da lista sem exibir numeros repetidos usando set
lista = [2, 3, 4, 2, 54, 5, 3, 3, 4, 3, 3]
print(f"Lista: {lista} com {len(lista)} elementos")

# Imprimindo os valores da tupla usando set
tupla = (2, 3, 4, 2, 4, 5, 2, 3, 2, 3, 56, 5, 4)
print(f"Tupla: {tupla} com {len(tupla)} elementos.")

# Criando um dicionario com os valores da primeira lista
dicionario = {}.fromkeys(lista, 'valor')
print(f"Dicionario: {dicionario} com {len(dicionario)} elementos.")

conjunto = {23, 54, 643, 64, 63, 78, 8, 4, 3, 8, 6}
print(f"Conjunto: {conjunto} com {len(conjunto)} elementos.")

# Criando uma lista com nomes de cidades repetidas
cidades = ["São Paulo", "Rio de Janeiro", "Ceará", "São Paulo", "Goiás", "Paraná", "Ceará"]

# Imprimindo a quantidade de cidades na lista e a quantidade de cidades distintas.
print(len(cidades))
print(len(set(cidades)))

# Criando um conjunto de dados
# Conjuntos-> possui ordenação propria
s = {1, 2, 3, 4}
s.add(5) # Adicionando valores no conjunto
print(s)
s.remove(2) # Removendo o valor e não o indice do conjunto.
s.discard(4) # Usado para remover o valor da indice passado por parametro
print(s)

estudante_python = {"Robson", "Roberto", "Thiago", "Lais", "Andre"}
estudante_java = {"Denis", "Carlos", "Rafael", "Wash", "Robson", "Lais"}

# Unindo as listas de conjuntos
new_estudantes = estudante_python.union(estudante_java)
print(new_estudantes)

# Forma 2 de uniao
estudantes = estudante_python | estudante_java
print(estudantes)

ambos1 = estudante_python.intersection(estudante_java)
print(ambos1)

# Forma 2
ambos2 = estudante_python & estudante_java
print(ambos2)

# Imprimindo estudantes de que não fazem o mesmo curso
so_python = estudante_python.difference(estudante_java)
so_java = estudante_java.difference(estudante_python)

print(so_python)
print(so_java)


