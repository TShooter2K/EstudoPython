"""
Fatiamento de strings
  012345678
  Olá mundo
 -987654321
fatiamento [i:f:p] [::] 
(i = inicio // f = fim // p = passo (quantos vai pular))

Obs.: a função len retorna a quantidade
de caracteres da str
"""

variavel = 'Olá mundo'
print(len(variavel[0:9:1]))
print(variavel[0:9:1])
print(variavel[0:9:2])
print(variavel[0:9:3])

print(variavel[::-1])
print(variavel[-1:-10:-1])