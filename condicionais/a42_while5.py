frase = 'O python é uma linguagem de programação '\
    'multiparadigma. '\
    'Phyton foi criado por Guido van Rossum.'.lower()

#print(frase.lower().count(''))

i = 0
qnt_que_apareceu = 0
letra_mais_repetida = ''

while i < len(frase):
    letra_atual = frase[i]

    if letra_atual == ' ':
        i += 1
        continue

    qnt_atual = frase.lower().count(letra_atual)

    if qnt_que_apareceu < qnt_atual:
        qnt_que_apareceu = qnt_atual
        letra_mais_repetida = letra_atual

    i += 1

print(f'A letra que apareceu mais vezes foi "{letra_mais_repetida}" '
      f'que apareceu {qnt_que_apareceu}x')