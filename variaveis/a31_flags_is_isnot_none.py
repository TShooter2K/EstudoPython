"""
Flag - Marcar um local
Nome = Não valor
is e is not = é ou não é (tipo, valor, identidade)
id = Identidade
"""

condicao = True
passou_no_if = None

if condicao:
    passou_no_if = True
    print('Faça algo')
else:
    print('Não faça nada')

# print(passou_no_if, passou_no_if is None)
# print(passou_no_if, passou_no_if is not None)

if passou_no_if is None:
    print('Não passou no if')
else:
    print('Passou no if')
    