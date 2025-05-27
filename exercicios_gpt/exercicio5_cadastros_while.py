"""
Objetivo:
Criar um programa onde o usuário pode cadastrar nomes (ex: de pessoas) e,
ao final, o programa mostra a lista completa de nomes cadastrados.
"""

nomes = []
nome = ''

while True:
    nome = input('Digite um nome para cadastro: ')

    if nome == '':
        print('Você precisa digitar um nome valido')
        continue

    nomes.append(nome)

    sair = input('Quer Sair [S]im ou [N]ão: ').lower().startswith('s')
    if sair:
        print(f'\n Você cadastrou {len(nomes)} nome(s): ')
        for item in nomes:
            print(item)
        break