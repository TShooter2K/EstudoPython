"""
Reoetições 
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira
Loop infinito -> Quando um code não tem fim
"""
contador = 0

while contador < 100:
    contador += 1

    if contador == 6:   # pula o 6
        print('nao vou mostrar o 6')
        continue        # volta no inicio e continua o code
  
    if 10 <= contador <= 27:
        #print('nao vou mostrar o', contador)
        continue

    print(contador)

    if contador == 40:
        break

print('Acabou')