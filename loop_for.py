"""
Utilizamos o loop para iterar sobre sequencias ou sobre valores iteraveis

Exemplos de iteraveis

String
nome = 'Robson Rodrigues'

lista
lista = [1,2,3,4,5,6,7,8,9,0]

Range
numeros range(1,100)

"""

nome = "Robson Rodrigues"

lista = [2, 1, 4, 32, 5, 6, 3, 56, 54, 54]

numeros = range(1, 51)

# Exibindo as letras da frase
for letra in nome:
    print(letra)

# Exibindo os numeros que estão dentro da lista
for numero in lista:
    print(numero)

# Valor do range nao pega o ultimo numero passado como parametro
for numero in numeros:
    print(numero)

# Enumerate -> adiciona um indice em cada caractere exibido no loop
for letra in enumerate(nome):
    print(letra)

# Coletando informações do usuario para criar um range de calculo
# qtd = int(input("Quantas vezes voce quer iterar?"))
# valores = []
# soma = 0
# for i in range(1, qtd+1):
#     num = int(input(f"Digite o {i}/{qtd} valor: "))
#     soma = soma + num
#     valores.append(soma)
# print(soma)
# print(valores)

value = "Robson"
print(value * 10)

# Usando a barra de escape antes do emoji unicode
for _ in range(5):
    for num in range(1, 6):
        print('\U0001F60D' * num)

