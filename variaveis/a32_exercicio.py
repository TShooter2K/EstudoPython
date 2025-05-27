"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

# numero_str = input('Digite um numero inteiro: ')
# # numero_int = int(numero_str)

# if numero_str.isdigit():
#     print('Este número é inteiro')

#     if int(numero_str) % 2 == 0:
#         print('Este número é par')
#     else:
#         print('Este número é ímpar')

# else:
#     print('Este número não é inteiro')


# # # resposta do professor

# # entrada = input('Digite um número: ')
# # if entrada.isdigit():
# #     entrada_int = int(entrada)
# #     par_impar = entrada_int % 2 == 0
# #     par_impar_texto = 'impar'
# #     if par_impar:
# #         par_impar_texto = 'par'
# #     print(f' o numero {entrada_int} é {par_impar_texto}')
# # else:
# #     print('voce nao digitou um numero inteiro')


# """
# Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
# descrito, exiba a saudação apropriada. Ex. 
# Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
# """

# hora_str = input('Informe as horas em números inteiros: ')
# hora = int(hora_str)

# if 0 <= hora <= 11:
#     print('Bom dia!')
# elif 12 <= hora <= 17:
#     print('Boa tarde!')
# elif 18 <= hora <= 23:
#     print('Boa noite!')
# else:
#     print('Não conheço essa hora! Por favor digite apenas números inteiros de 0 a 23 horas')


"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

nome = input('Qual o seu primeiro nome? ')
tamanho_nome = len(nome)

if nome:
    print(f'Seu nome é {nome}')
    print(f'seu nome possui {tamanho_nome} letras')

    if tamanho_nome <= 4:
        print('Seu nome é curto')
    elif 5 <= tamanho_nome <= 6:
        print('Seu nome é normal')
    elif tamanho_nome > 6:
        print('Seu nome é muito grande')
else:
    print('Você não digitou nada! Por favor digite seu nome.')