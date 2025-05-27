"""
Peça nome, peso (kg) e altura (m) do usuário. Calcule o IMC com a fórmula:
IMC = peso / (altura ** 2)

Dê uma classificação com base no resultado:
Abaixo de 18.5: Abaixo do peso
18.5 a 24.9: Peso normal
25 a 29.9: Sobrepeso
30 ou mais: Obesidade
"""

# CODIGO BÁSICO (SEM AJUDA)

nome = input('Qual seu nome? ')
altura = input('Qual sua altura (em metros)? ')
peso = input('Qual seu peso (em kg)? ')

peso_float = float(peso)
altura_float = float(altura)

imc = peso_float / (altura_float * altura_float)

if imc <= 18.4:
    print(f'{nome} seu IMC é {imc:.2f} e você está abaixo do peso')
elif 18.5 <= imc <= 24.9:
    print(f'{nome} seu IMC é {imc:.2f} e você está no peso normal')
elif 25 <= imc <= 29.9:
    print(f'{nome} seu IMC é {imc:.2f} e você está com sobrepeso')
elif imc > 30:
    print(f'{nome} seu IMC é {imc:.2f} e você está com obesidade')
else:
    print('Você digitou algum dado errado, tente novamente!')


# # CODIGO MAIS ROBUSTO  (dicas gpt, ainda não sei oque é replace)

# nome = input('Qual seu nome? ')
# altura = input('Qual sua altura (em metros)? ')
# peso = input('Qual seu peso (em kg)? ')

# # Verifica se altura e peso são números válidos (float)
# if altura.replace('.', '', 1).isdigit() and peso.replace('.', '', 1).isdigit():
#     peso_float = float(peso)
#     altura_float = float(altura)

# # Verifica se são positivos
#     if altura_float > 0 and peso_float > 0: 
#         imc = peso_float / (altura_float * altura_float)

#         if imc <= 18.4:
#             print(f'{nome} seu IMC é {imc:.2f} e você está abaixo do peso')
#         elif 18.5 <= imc <= 24.9:
#             print(f'{nome} seu IMC é {imc:.2f} e você está no peso normal')
#         elif 25 <= imc <= 29.9:
#             print(f'{nome} seu IMC é {imc:.2f} e você está com sobrepeso')
#         elif imc > 30:
#             print(f'{nome} seu IMC é {imc:.2f} e você está com obesidade')
#     else:
#         print('Peso e altura precisam ser maiores que zero.')
# else:
#     print('Digite apenas números válidos com ponto (.) se necessário, não aceitamos virgula (,).')