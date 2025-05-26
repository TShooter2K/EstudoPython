"""
For = para
While usado para repetições infinitas 
For usado quando sabemos o final da repetição
"""

# Exemplo com while infinito

# senha_salva = '123456'
# senha_digitada = ''
# repeticoes = 0

# while senha_salva != senha_digitada:
#     senha_digitada = input(f'Sua senha ({repeticoes}x): ')

#     repeticoes += 1

# print(repeticoes)
# print('Aquele laço acima pode ter repetições infinitas')


# Com for, repetição com final
texto = 'Python'
novo_texto = ''

# For = Para 'para letra' 
for letra in texto:
    novo_texto += f'*{letra}'
    #print(letra)
print(novo_texto + '*')
