"""
Peça ao usuário para digitar um CPF (apenas números), faça:
    Verificação se tem 11 dígitos
    Se só contém números
    Exiba o CPF no formato 000.000.000-00
    Ex.: Entrada: 12345678912 Saida: 123.456.789-12
"""


cpf_usuario = input('Digite seu CPF sem pontuação: ')
tamanho_cpf = len(cpf_usuario)
# tamanho_cpf_int = int(cpf_usuario)

if cpf_usuario.isdigit() and tamanho_cpf == 11:
    # print(f'Seu CPF tem {tamanho_cpf} digitos')
    print(f'Seu CPF é {cpf_usuario[:3]}.{cpf_usuario[3:6]}.{cpf_usuario[6:9]}-{cpf_usuario[9:]}')
else:
    print('CPF inválido! Digite 11 dígitos como no exemplo.: 00000000000 ')


