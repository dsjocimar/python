# Exercício 091

from random import randint
from time import sleep
from operator import itemgetter
jogadas = dict()
ranking = list()
for c in range(0, 4):
    jogadas[f'jogador{c}'] = randint(1, 6)
print('VALORES SORTEADOS:')
for k, v in jogadas.items():
        print(f'    O {k} tirou {v}')
        sleep(1)
print('=-'*20)
print('     RANKING DOS JOGADORES:')
ranking = sorted(jogadas.items(),key=itemgetter(1),reverse=True)
for i, v in enumerate(ranking):
    print(f'    {i+1}º LUGAR: {v[0]} COM {v[1]}.')
    sleep(1)
