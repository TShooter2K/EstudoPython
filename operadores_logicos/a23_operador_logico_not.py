# operador lógico "not"
# usado para inverter expressões 
# not True = False
# not False = True

# print(not True) # False
# print(not False) # True

senha = input('Senha: ')

# if senha == '123':
#     print('Entrou')
# else:
#     print('Senha incorreta')

if not senha:
    print('Você não digitou nada')