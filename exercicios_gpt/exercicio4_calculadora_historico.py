""" Calculadora com while """

# Lista para guardar valores
historico = []

while True:
    # Armazena as variaveis
    numero1 = input('Digite o primeiro numero: ')
    numero2 = input('Digite o segundo numero: ')
    operador = input('Digite um operador (+-/*): ')
    numeros_validos = None

    num1_float = 0
    num2_float = 0

    # Verifica se os numeros sao validos
    try:
        num1_float = float(numero1)
        num2_float = float(numero2)
        numeros_validos = True
    except:
        numeros_validos = None 
    
    # Se for valido segue para proxima parte
    if numeros_validos is None:
        print('Um dos números digitados são inválidos')
        continue
    
    operadores_permitidos = '+-/*'

    # Verifica se os operadores estão na variavel
    if operador not in operadores_permitidos:
        print('Operador inválido.')
        continue
    
    # Verifica se foi digitado apenas 1 operador
    if len(operador) > 1:
        print('Digite apenas um operador.')
        continue

    # Faz a conta e armazena na variavel
    print('Confira o resultado da sua conta:')
    if operador == '+':
        resultado = num1_float + num2_float
    elif operador == '-':
        resultado = num1_float - num2_float
    elif operador == '/':
        resultado = num1_float / num2_float
    elif operador == '*':
        resultado = num1_float * num2_float
    
    # Mostra o resultado
    print(f'Resultado: {num1_float} {operador} {num2_float} = {resultado}')

    # Salva o historico
    historico.append(f'{num1_float} {operador} {num2_float} = {resultado}')
        
    # Sai da calculadora
    sair = input('Quer sair? [s]im: ').lower().startswith('s')

    if sair:
        print('\n Historico de operações: ')
        for item in historico:  # Mostra historico
            print(item)         # Mostra historico
        break # Para o codigo