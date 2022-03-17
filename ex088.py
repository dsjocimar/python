# Exercício 088

from random import randint
from time import sleep

jogo = list()
print('=-' * 15)
print(f'{"JOGA NA MEGA SENA":^30}')
print('-=' * 15)
n = int(input('Quantos jogos você quer que eu sorteie? '))
print(f'=-' * 4, 'Sorteando', n, 'jogos', '=-' * 4)
for c in range(0, n):
    print(f'Jogo', c + 1, ': ', end='')
    for d in range(0, 6):
        jogo.append(randint(0, 60))
    print(jogo)
    jogo.clear()
    sleep(1.5)
print(f'=-'*5, '< Boa sorte! >', '=-'*5)
