# Exercício 092

from datetime import date
hoje = date.today().year
trabalhador = dict()
trabalhador['nome'] = str(input('Digite o seu nome: '))
nasc = int(input('Digite o seu ano de nascimento: '))
trabalhador['idade'] = hoje - nasc
trabalhador['ctps'] = int(input('Carteira de trabalho (0 não tem): '))
if trabalhador['ctps'] == 0:
    print('=-'*30)
    for k, v in trabalhador.items():
        print(f'{k} tem o valor de {v}')
else:
    trabalhador['salário'] = float(input(f'Salário: R$ '))
    trabalhador['contratação'] = int(input('Ano da contratação: '))
    trabalhador['aposentadoria'] = (trabalhador['contratação'] + 35) - nasc
    print('-='*30)
    for k, v in trabalhador.items():
        print(f'{k} tem o valor de {v}')




