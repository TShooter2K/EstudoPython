"""
Cuidados com dados mútaveis
= - copiado o valor (imutáveis)
= - aponta para o mesmo valor na memória (mutável)
"""

# nome = 'Patrick'
# outra_variavel = nome   # quarda o valor da primeira variavel (patrick)
# nome = 'Marques'        # muda o valor da variavel (marques)
# print(outra_variavel, nome)

lista_a = ['Luiz', 'Maria', 1, 4, 1.2]
lista_b = lista_a.copy()    # copia a lista_a para a lista_b, alteração
                            # posteriores não entram, vira imutável.

lista_a[0] = 'qualquer coisa'
print(lista_b)  # mostra a lista_b depois da copia.
print(lista_a)  # mostra a lista_a com as alterações