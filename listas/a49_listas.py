"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis: 
    append, insert, pop, del, clear, extend, +
Create, Read, Update   Delete
Criar,  ler,  alterar, apagar = lista[i] (CRUD)
""" 
"""
remover um indice faz com que todos os após sejam movidos
se a lista tiver muitos valores (ex: 1kk de numeros) pode exigir
muito processamento e travar, é recomendado o uso com cautela 
del lista[2]
"""

#        0   1   2   3   4    6  => se apagar um indice todos se movem (mudam de valor)
lista = [10, 20, 30, 40, 50, 60]
# lista[2] = 300
lista.append(70)    # adiciona um valor ao final da lista (70)
valor_removido1 = lista.pop()   # remove o ultimo valor da lista (70)
lista.append(80)
lista.append(90)
valor_removido2 = lista.pop() 
print(lista, 'Os valores removidos foram: ', valor_removido1, valor_removido2)
# print(lista[2])