"""
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você 
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.
"""
import random

palavras = [
    'abacaxi', 'montanha', 'programador', 'cachorro', 
    'inteligencia', 'chuva', 'bicicleta', 'girassol',
    'cala boca', 'pinguim', 'universo'
]

palavra_secreta = random.choice(palavras).lower()
tentativas = 0 
progresso = ["*"] * len(palavra_secreta)
letras_usadas = set()

for i, letra_da_palavra in enumerate(palavra_secreta):
    if letra_da_palavra == ' ':
        progresso[i] = ' '

while True:
    letra_digitada = input('Digite uma letra: ').lower()

    # Verifica se é apenas uma letra
    if len(letra_digitada) != 1 or not letra_digitada.isalpha():
        print('Digite apenas UMA letra válida de (A-Z).')
        continue
    # Verifica se a letra foi usada
    if letra_digitada in letras_usadas:
        print(f"Você já tentou a letra '{letra_digitada}', tente outra!")
        continue

    # Adiciona letra tentada ao conjunto!
    letras_usadas.add(letra_digitada)
    # soma +1 a tentativa
    tentativas += 1
    acertou = False

    for i, letra_da_palavra in enumerate(palavra_secreta):
        if letra_digitada == letra_da_palavra:
            progresso[i] = letra_digitada
            acertou = True
            
    print('\n'+ ''.join(progresso))

    if not acertou:
        print(f"A letra '{letra_digitada}' não está na palavra.")

    if '*' not in progresso:
        print(f'\n Parabéns! Você descobriu a palavra "{palavra_secreta}"'
              f' em {tentativas} tentativas')
        break