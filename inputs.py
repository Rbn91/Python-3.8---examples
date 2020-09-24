"""
 input - Serve para pegar dados digitados pelo usuario do sistema
 Todos os dados recebido via input é uma string
 em python tudo é string que estiver dentro de aspas
"""

nome = input("Digite seu nome: ")

# exemplo de print antigo versao 2.x
print("Seja bem vindo(a) %s" % nome)

# exemplo de print versao 3
print("Seja bem vinda(o) " + nome)

# exemplo de print versao 3.3
print("qual o seu nome?")
nome = input()

print("Qual a sua idade?")
idade = input()

# exemplo de print versao 3.5
print("Seu nome {0} e sua idade é {1}".format(nome, idade))

# exemplo de print atual da versao 3.7
print(f'Seu nome é {nome} e sua idade é {idade} anos')

# calculando a idade direto no print
# cast - é uma conversao de uma variavel do tipo string para o tipo inteiro
print(f"O {nome} nasceu no ano de {2020 - int(idade) - 1}")

