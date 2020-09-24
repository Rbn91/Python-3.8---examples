"""
    Metodos condicionais feitas em python
    if, else, elif
    AND, OR, NOT, IS

"""

numero = 32

# condicional usando operadores logicos
if numero <= 12:
    print(numero)
else:
    print(f"Numero é maior que {numero}")

# condicional usando elif

if numero <= 18:
    print("voce é menor de idade!")
elif numero > 18 and numero <= 50:
    print("voce ainda pode curtir a vida")
else:
    print("voce esta muito velho")

# condicional usando or
if numero == 23 or numero == 32:
    print("numero equivalente")
else:
    print('numero nao é equivalente')

# condicional usando not - se nao estiver ativo
valor = True

if not valor:
    print('não e o valor')
else:
    print("é o valor")

print(valor is False)

