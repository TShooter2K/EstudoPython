"""
Exercício 
Exiba os índices da lista
ex.:
0 Maria
1 Helena
2 Patrick

De forma dinamica para caso adicione
mais itens a lista
"""

lista = ['Maria', 'Helena', 'Patrick']
i = 0

lista.append('Lucas')   # adiciona o valor Lucas a lista 

# Enumerate percorre um iterável e retorna dois valores em cada iteração:
#   O índice (posição) do elemento.
#   O valor do elemento
for i, nome in enumerate(lista): # pega indice e nome dos valores da variavel lista
    print(i, nome) 
        