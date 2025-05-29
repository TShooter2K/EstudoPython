""" 
Enumerate - enumera iteráveis (indices)
"""

lista = ['Maria', 'Luiz', 'Patrick']
lista.append('João')

# Após passar pelo enumerate dentro de uma variavel a lista fica vazia!
# Enumerate consome os dados apenas 1x
# lista_enumerada = enumerate(lista)

# Fora da variavel criando um eterator por vez ele le todas!
for item in enumerate(lista):
    # a = indice b = item
    a, b = item
    print(a, b)

for indice, nome in enumerate(lista):
    print(indice, nome)

# for item in enumerate(lista):
#     print(item)
# for item in enumerate(lista):
#     print(item)

# print('O que tem na lista enumerada', lista_enumerada)

for tupla_enumerada in enumerate(lista):
    print('For da tupla: ')
    for valor in tupla_enumerada:
        print(f'{valor}')


# lista_enumerada = list(enumerate(lista))
# print(lista_enumerada)

