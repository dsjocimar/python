# Exercício 045

from random import randint

print('\033[1;32m=-' * 10)
print('       JOKONPÔ')
print('-=' * 10, '\033[m')
n = str(input('VAMOS JOGAR JOKEPÔ? '))
if n == 'sim' or n == 'SIM':
    escolha = int(input('SELECIONE\n[0] - PEDRA\n[1] - PAPEL\n[2] - TESOURA\n '))
    if 0 <= escolha <= 2:
        lista = ['PEDRA', 'PAPEL', 'TESOURA','OPÇÃO INVÁLIDA']
        n = randint(0, 2)
        computador = lista[n]
        usuario = lista[escolha]
        if usuario == computador:
            print(f'DEU EMPATE! OS DOIS JOGARAM {usuario}')
        elif usuario == lista[0]:
            if computador == lista[1]:
                print(f'QUE PENA, EU VENCI! VOCÊ ESCOLHEU {usuario} E EU ESCOLHI {computador}')
            else:
                print(f'PARABÉNS! VOCÊ ME VENCEU! VOCÊ ESCOLHEU {usuario} E EU ESCOLHI {computador}')
        elif usuario == lista[1]:
            if computador == lista[0]:
                print(f'PARABÉNS! VOCÊ ME VENCEU! VOCÊ ESCOLHEU {usuario} E EU ESCOLHI {computador}')
            else:
                print(f'QUE PENA, EU VENCI! VOCÊ ESCOLHEU {usuario} E EU ESCOLHI {computador}')
        elif usuario == lista[2]:
            if computador == lista[0]:
                print(f'QUE PENA, EU VENCI! VOCÊ ESCOLHEU {usuario} E EU ESCOLHI {computador}')
            else:
                print(f'PARABÉNS! VOCÊ ME VENCEU! VOCÊ ESCOLHEU {usuario} E EU ESCOLHI {computador}')
    else:
        print('\033[1;31mOPÇÃO INVÁLIDA! TENTE NOVAMENTE!\033[m')
else:
    print('OBRIGADO PELA ATENÇÃO!')

'''from random import randint

itens = ['pedra', 'papel', 'tesoura']
computador = randint(0, 2)
print(itens[computador])'''
