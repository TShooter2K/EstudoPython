"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis:
    append - Adiciona um item ao final
    insert - Adiciona um item no índice escolhido
    pop - Remove do final ou do índice escolhido
    del - apaga um índice
    clear - limpa a lista
    extend - estende a lista
    + - concatena listas
Create, Read, Update   Delete
Criar,  ler,  alterar, apagar = lista[i] (CRUD)
"""
#        0   1   2   3
lista = [10, 20, 30, 40]
lista.append('patrick') # Adiciona um item ao final
nome = lista.pop()
lista.append(1233)
del lista[-1]   # apaga um índice
# lista.clear() # limpa a lista
lista.insert(0, 5)  # Adiciona um item no índice escolhido 
                    # primeiro valor é local onde vai ser inserido
                    # segundo valor é o valor que sera inserido
print(lista)