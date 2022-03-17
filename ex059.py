# Exercício 059

n1 = float(input('Digite um valor: '))
n2 = float(input('Digite outro valor: '))
n = 1
while 0 < n < 5:
    print('''====MENU DE SELEÇÃO==== 
[1] - SOMAR 
[2] - MULTIPLICAR 
[3] - MAIOR 
[4] - NOVOS NÚMEROS 
[5] - SAIR DO PROGRAMA''')
    n = int(input('OPÇÃO SELECIONADA: '))
    if n == 1:
        print(f'A soma de {n1} com {n2} vale {n1 + n2}')
    elif n == 2:
        print(f'O produto de {n1} com {n2} vale {n1 * n2}')
    elif n == 3:
        if n1 > n2:
            print(f'O maior número é o {n1}')
        elif n1 < n2:
            print(f'O maior número é o {n2}')
        else:
            print(f'Os dois números são iguais e valem {n1}')
    elif n == 4:
        n1 = float(input('Digite um novo valor: '))
        n2 = float(input('Digite mais um novo valor: '))
    print('')
print('SAINDO...')
