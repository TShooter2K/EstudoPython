# For i vai de 0 a 9 e for j vai de 1 a 2 
# for i = linhas --- for j = colunas

# cria linhas de 0 a 9
for i in range(10):
    # verifica se i é igual a 2
    if i == 2:
        print('i é 2, pulando...')
        continue
    # verifica se i é igual a 8
    if i == 8:
        print('i é 8, seu else não executará')
        break # finalisa o laço e não executa o else
    
    # cria colunas de 1 a 2
    for j in range(1, 3):
        # mostra(printa) linhas e colunas
        print(i, j)

# só executa se o laço for completo
else:
    print('For completo com sucesso!') 