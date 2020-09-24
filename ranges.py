"""
    É preciso conhecer lacos de repeticao para trabalhar melhor com o range

    Metodos de definicao de range
     - range(valor_final) - vai gerar valores até o valor passado por parametro -1.
     - range(valor_inicio, valor_final) - Define um intervalo de valores a serem carregados.
     - rande(valor_inicio, valor_final, passos) - define um intervalo de valores a serem carregados e o passo Ex: 2 em 2.
"""

# Preencehndo lista com range
lista = list(range(0, 100))
print(lista)

# Usando um laco para percorrer um range de 10 posicoes
for num in range(0, 10):
    print(num)

# leambrando que o passo final, o python imprime até o seu antecessor.
lista_par = list(range(0, 10, 2))
print(lista_par)

# Efetuando o laco com o valor inverso do range
for value in range(20, -1, -1):
    print(value)
