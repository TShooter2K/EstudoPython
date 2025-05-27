"""
Crie um sistema com usuário e senha fixos no código. Peça para o usuário digitar ambos:
Se ambos estiverem corretos, imprima "Login realizado com sucesso!"
Caso contrário, mostre qual dos campos está incorreto.
"""

login_usuario = input('Digite seu login: ')
senha_usuario = input('Digite sua senha: ')

login_registrado = 'admin'
senha_registrado = '123456'

if  login_usuario == login_registrado and senha_usuario == senha_registrado:
    print('Login realizado com sucesso!')
else:
    print('Login ou Senha incorretos, tente novamente!')