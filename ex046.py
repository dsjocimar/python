# Exercício 046

from time import sleep

contador = 10
for contador in range(contador, -1, -1):
    print(contador, '...')
    sleep(1)
print('ACIONEM OS FOGOS!')
