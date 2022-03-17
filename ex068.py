# Exercício 068

from random import randint

print('-=' * 13)
print(' VAMOS JOGAR PAR OU ÍMPAR')
vitoria = 0
while True:
    total = 0
    computador = randint(0, 10)
    print('-=' * 13)
    n_jogador = int(input('Diga um valor: '))
    s_jogador = str(input('Par ou Ímpar? [P/I] ')).strip().upper()[0]
    while s_jogador not in 'PI':
        s_jogador = str(input('OPÇÃO INVÁLIDA! Escolha denovo apenas Par ou Ímpar [P/I]')).strip().upper()[0]
    total = computador + n_jogador
    pi = total % 2
    if pi == 0:
        print('--' * 13)
        print(f'Você jogou {n_jogador} e o computador jogou {computador}. Total de {total} DEU PAR')
        print('--' * 13)
        if s_jogador == 'P':
            print('Você VENCEU!')
            print('Vamos jogar novamente...')
            vitoria += 1
        else:
            print(f'Você PERDEU!')
            break
    else:
        print('--' * 13)
        print(f'Você jogou {n_jogador} e o computador jogou {computador}. Total de {total} DEU ÍMPAR!')
        print('--' * 13)
        if s_jogador == 'I':
            print('Você VENCEU!')
            print('Vamos jogar novamente...')
            vitoria += 1
        else:
            print(f'Você PERDEU!')
            break
print(f'GAME OVER! Você venceu {vitoria} Vezes.')



