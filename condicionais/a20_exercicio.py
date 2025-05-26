# Comparar os dois valores e mostrar na tela "Valor x é maior que valor y"
# O valor maior deve vir primeiro

primeiro_valor = input('Digite um valor: ')
segundo_valor = input('Digite outro valor: ')

if primeiro_valor > segundo_valor:
    print(f'O valor {primeiro_valor} é maior que {segundo_valor}!')
elif segundo_valor > primeiro_valor:
    print(f'O Valor {segundo_valor} é maior que {primeiro_valor}!')
else:
    print('Os valores são iguais!')