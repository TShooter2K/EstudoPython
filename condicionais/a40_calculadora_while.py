""" Calculadora com while """

while True:
    numero1 = input('Digite o primeiro numero: ')
    numero2 = input('Digite o segundo numero: ')
    operador = input('Digite um operador (+-/*): ')
    numeros_validos = None

    num1_float = 0
    num2_float = 0

    try:
        num1_float = float(numero1)
        num2_float = float(numero2)
        numeros_validos = True
    except:
        numeros_validos = None
    
    if numeros_validos is None:
        print('Um dos números digitados são inválidos')
        continue
    
    operadores_permitidos = '+-/*'

    if operador not in operadores_permitidos:
        print('Operador inválido.')
        continue
    
    if len(operador) > 1:
        print('Digite apenas um operador.')
        continue

    print('Confira o resultado da sua conta:')
    if operador == '+':
        print(f'{num1_float} + {num2_float} = ', num1_float + num2_float)
    elif operador == '-':
        print(num1_float - num2_float)
    elif operador == '/':
        print(num1_float / num2_float)
    elif operador == '*':
        print(num1_float * num2_float)
    

    sair = input('Quer sair? [s]im: ').lower().startswith('s')

    if sair is True:
        break


