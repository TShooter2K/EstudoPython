""" 
Introdução ao desempacotamento + tuples (tuplas)
"""

# nome1, nome2, nome3 = ['Maria', 'Helena', 'Patrick']
_, nome, *_ = ['Maria', 'Helena', 'Patrick']
print(nome)
# print(_)