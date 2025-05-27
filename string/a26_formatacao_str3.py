"""
Formatação básica de strings
s - string 
d - int
f - float
.<número de dígitos>f
x ou X - hexadecimal
(caractere)(><^)(quantidade)
> - Esquerda
< - Direita
^ - Centro
= - Força o número a aparecer antes dos zeros
Sinal - + ou -
Ex.: 0>-100,.1f
Conversion flags - !r !s !a
"""

variavel = 'ABC'
print(f'{variavel}')

# : mais qual caracter deseja, direção e quantidade 

# : >10 - adiciona 10 caracteres vazios a esquerda
print(f'{variavel: >10}')
# :.>10 - adiciona 10 caracteres '.' a direita
print(f'{variavel:.<10}')
# :_>10 - adiciona 10 caracteres '_' divididos esqueda e direita
print(f'{variavel:_^10}')

print(f'{1000.46543515648:,.2f}')
print(f'{1000.46543515648:0=+10,.2f}')
print(f'O hexadecimal de 1500 é {1500:08X}')
print(f'{variavel!r}')