"""
Iterável => str, range, etc
    __iter__ (metodo)
Iterador => quem sabe entregar um valor por vez
Next => me entrega o proximo valor
Iter => me entrega seu iterador


"""

# texto = iter('Patrick') # verifica o iterator ou .__iter__() 

# print(next(texto)) # chama o proximo valor ou .__next__()
# print(next(texto))
# print(next(texto))
# print(next(texto))


""" usando While para explicar como funciona o FOR"""
# texto = 'Patrick' # iteravel
# iterador = iter(texto) # iterador
# while True:
#     try:
#         letra = next(iterador)
#         print(letra)
#     except StopIteration:
#         break

# Fazendo a mesma coisa com o For
texto = 'Patrick' # iteravel
for letra in texto:
    print(letra)