"""
manipulando numeros em python
"""
"""
MANIPULANDO NUMEROS INTEIROS
"""
valor1 = 10
valor2 = 20

adicao = valor1 + valor2
subtracao = valor1 - valor2
multiplicacao = valor1 * valor2
divisao = valor1 / valor2
resto = valor1 % valor2
potencia = valor1**valor2

print("total: {0}".format(adicao))
print(f"total: {subtracao}")
print(multiplicacao)
print(divisao)
print(resto)
print(potencia)
print(type(valor2))

"""
MANIPULANDO NUMEROS FLOAT
"""
# metodo errado, onde ele vai pegar a variavel e formar uma tupla
valor = 1, 44
print(valor)

# certo do ponto de vista FLOAT
valor3 = 1.44
print(valor3)
print(type(valor3))

# python permite dupla atribuicao
valor4, valor5 = 1, 2
print(valor4)
print(valor5)

# convertendo de float para int
valor6 = 12.23
new_value = int(valor6)
print(valor6)
print(new_value)

# **************************************

"""
MANIPULANDO NUMEROS BOLEANOS
    - tipos booleanos sao definidos em python com letras maiusculas 
"""
ativo = False
desativado = True
print(ativo)
print(desativado)
print(not ativo)  # negacao
print(not desativado)  # negacao

# **************************************

"""
 MANIPULANDO STRINGS
  - um dado sempre sera uma string se estiver dentro de aspas simples ou duplas ou triplas.
"""

nome = """Robson"""
print(nome)
print(type(nome))

name = "Angelina \nJolie"
print(name)

name2 = """Nicolas
Cage"""
print(name2)

print(nome.upper())  # transforma para maiusculo
print(name.lower())  # transforma para minusculo
print(name2.split())  # quebra os valores no espaco e adiciona em uma lista
print(name2.split()[0])  # imprimindo a primeira posicao antes do espaco
print(nome[0:3])  # Slice de string
print(name2[::-1])  # invertendo toda a frase. Modo pytonico.
print(nome.replace("n", "m"))

# **************************************
