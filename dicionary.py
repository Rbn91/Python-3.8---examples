"""
 Dicionarios em python

 dicionarios sao coleções de chave e valor representados por {}

 OBS:
    - -Chave e valor são separados por dois pontos 'chave:valor'.
    - tanto chave como valor podem ser de qualuqer tipo de dados.
    - podemos misturar tipos de dados.

Criação de dicionarios

"""
# Primeiro metodo de escrever um dicionario
paises = {'eua': 'estados unidos', 'brazil': 'Brasil', 'germany': 'Alemanha'}

print(paises)
print(type(paises))

# Segundo metodo de escrever um dicionario
paises = dict(eua='Brazil', brazil='united states', germany='Alemanha')

print(paises)
print(type(paises))

# Acessando elementos e imprimindo do dicionario
print(paises['eua'])
# Forma recomendada para se acessar uma valor de um dicionario
valor = paises.get('germany')
print(valor)

# Forma de atribuir um valor e uma chave inexistente dentro do dicionario
# Atribuindo um valor a uma chave inexistente no dicionario
pais = paises.get('ru', 'Não possui esse valor')
print(pais)

# Adicionando valores no dicionario

precos = {'jan': '2.00', 'fev': '6.45', 'mar': '23.22'}

print(precos)

precos['abr'] = 4.32

print(precos)

# Segunda forma de adicionar o valor de um dicionario
new_value = {'mai': 12}
precos.update(new_value)
print(precos)

# Adicionando um novo valor no mes de maio
precos.update({'mai': 13})
print(precos)

# CONCLUSÃO: A forma de adicionar dados no dicionario é a mesmo de update.
# CONCLUSÃO: Em dicionarios, não podemos ter chaves repetidas.

# Removendo dados de um dicionario

paises = {'brasil': 'sao paulo', 'franca': 'paris', 'alemanha': 'berlin', 'chile': 'san thiago'}
print(paises)


# primeira forma de remover usando POP
paises.pop('chile')
print(paises)

# Segunda forma de remover usando DEL
del paises['franca']
print(paises)

# Usando tuplas, listas e dicionarios para preencher um carrinho

carrinho1 = []
carrinho2 = []
carrinho3 = []

# Usando Lista

produto1 = ['Playstation 4', 1, 2.300]
produto2 = ['Iphone', 2, 4000]

carrinho1.append(produto1)
carrinho1.append(produto2)

print(carrinho1)

# Usando Tuplas

produto3 = ('Playstation 4', 3, 2333)
produto4 = ('Computador gamer', 1, 6000)

carrinho2.append(produto3)
carrinho2.append(produto4)

print(carrinho2)

# Usando dicionario

produto5 = {'produto': 'Playstation', 'quantidade': 4, 'valor': 5000}
produto6 = {'produto': 'computador gamer', 'quantidade': 1, 'valor': 4000}

carrinho3.append(produto5)
carrinho3.append(produto6)

print(carrinho1)
print(carrinho2)
print(carrinho3)

# Metodos de dicionarios
# Copiando um dicionario

numeros = dict(a=23, b=1, c=4, d=3)
print(numeros)

new_numeros = numeros.copy()
new_numeros['e'] = 32
print(new_numeros)

# Metodo não usual de criar um dicionario
outro = {}.fromkeys('a', 'b')
print(outro)

# Adicionando o mesmo valora para diversas chaves dentro de um dicionario
usuario_mesmo_valor = {}.fromkeys(['nome', 'idade', 'endereco', 'email'], 'null')
print(usuario_mesmo_valor)

# Usando o fromkeys para iterar um valor em um dicionario
novo_nome = {}.fromkeys('onibus', 'null')
print(novo_nome)

# Usando o range para determinar chaves com o mesmo valor dentro de um dicionario
dic_com_range = {}.fromkeys(range(1, 50), 'null')
print(dic_com_range)

"""
 tipo Nome
 
 O tipo de dados Nome em python representa o tipo sem tipo. ou poderia ser conhecido tambem como tipo
 vazio, porem, falar que é um tipo sem tipo é mais apropriado.
 
 Certo: None
 Errado: none
 
 quando utilizar
  - Quando criamos uma variavel para receber um valor e não queremos definir um tipo para essa variavel,
  antes mesmo de ela receber algum valor.
 
"""

numero = None
print(numero)
print(type(numero))



