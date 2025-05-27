# Operadores in e not in
# (está entre ou não está entre)
# Strings são iteráveis
#  0 1 2 3 4 5
#  O t á v i o
# -6-5-4-3-2-1

# 0 1 2 3 4 5 6 
# P A T R I C K
# -7-6-5-4-3-2-1

# nome = 'Patrick'
# print(nome[3])
# print(nome[-2])
# print(10 * '-')

# # Está entre
# print('t' in nome)
# print('x' in nome)
# print('xau' in nome)
# print(10 * '-')

# # Não está entre
# print('x' not in nome)
# print('xau' not in nome)

nome = input('Digite seu nome: ')
encontrar = input('Digite o que deseja encontar: ')

if encontrar in nome:
    print(f'{encontrar} está em {nome}')
else:
    print(f'{encontrar} não está em {nome}')