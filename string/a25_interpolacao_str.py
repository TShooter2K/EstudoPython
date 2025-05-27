"""
Interpolação básica de strings
s - string
d e i - int
f - float
x e X - hexadecimal (ABCDEF123456789)
"""

nome = 'Patrick'
preco = 1000.95897643
variavel = '%s, o preço total foi R$%.2f' %(nome, preco)
print(variavel)

print('O hexadecimal de %d é %04X' %(15, 15)) 