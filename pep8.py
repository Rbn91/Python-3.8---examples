"""
    Comandos para iniciar o poema do python na PEP8

    A ideia da PEP8 é que possamos escrever codigos python de forma exemplar.
    forma pythônica, método agradável.

    [1] - Utilize Camel case para nome de classes;

    class Calculadora:
        pass

    class CalculadoraAutomatica:
        pass

    [2] - utilize nomes minusculos separados com underlines para funcoes e variaveis;

    def soma():
        pass

    def Soma_dois_valores():
        pass

    numero = 4
    segundo_numero = 5

    [3] - utlize 4 espacos para a identacao;

    if numero == 4:
        print('existe')

    [4] - linhas em branco, separar funcoes e definicoes de classe com 2 linhas em branco;
        - metodos dentro da classe deve ser separado com apenas 1 linha em branco dentro da classe;

    [5] - imports deve ser sempre feitos em linhas separadas;

    import beatifulsoup
    import numpy
    import panda

    -outro tipo de impor de varias classes de uma mesma biblioteca é:
        import types (
            typeOne,
            typeTwo,
            typeThree,
            typeFour
        )
    imports sempre sera colocado no topo do arquivo em que esta sendo chamado;

    [6] - Espaços em expressões e instruções;

      - funcao(algo[1], {algo: 2})

      - algo(1)

      - dict['chave'] = list[valor]

    DIR - apresenta todos os atributos e funcoes/metodos para determindado tipo de dados ou variavel
    help - apresenta a documentacao de como se usar aquela variavel, funcao ou atributo que esta setada.
"""
import this

print("Teste de desenvolvimento")

num = 5



print(num.__add__(5))


