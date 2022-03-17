# Exercício 028
from random import randint
from time import sleep
escolhido = randint(0,5)    # Faz o computador pensar
print('=-' * 20)
escolha = int(input('''Tente adivinhar qual número o computador pensou, 
de 0 a 5: '''))             # Faz o jogador tentar adivinhar
print('PROCESSANDO...VAMOS VER SE VOCÊ GANHOU OU NÃO')
sleep(2)
if escolha == escolhido:
    print(f'VOCÊ GANHOU! PENSAMOS NO MESMO NÚMERO, o \033[1;33m{escolhido}\033[m')
else:
    print(f'VOCÊ PERDEU! Você pensou no número \033[1;31m{escolha}\033[m, mas eu pensei no número \033[1;32m{escolhido}\033[m')