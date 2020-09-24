"""
    LOOP WHILE -> Expressão boolean onde precisa ter uma valor falso para terminar o laco
    BREAK -> Usado para encerrar lacos de repeticao
"""

num = 1

# Determinando um limite para o loop executar
while num <= 10:
    print(num)
    num = num + 1

# Enquanto a resposta digitada não for igual o calor da condicao, o laco continua executando.
answer = ''
while answer != 'yes':
    answer = input("Do you wanna drink some beer?")


# O laco de repeticao para de excutar quando o laco chega no valor determinado no if dentro do loop.
value = 1
while value <= 20:
    if value == 5:
        break
    print(value)
    value = value + 1

