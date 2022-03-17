# Exercício 058

from random import randint
tentativas = 0
computador = randint(0, 10)
jogador = int(input('TENTE ADIVINHAR QUAL NÚMERO EU ESTOU PENSANDO, DE 0 A 10...'))
print('PROCESSANDO...')
while jogador != computador:
    jogador = int(input('VOCÊ ERROU! TENTE NOVAMENTE!:\n'))
    tentativas += 1
if tentativas == 0:
    tentativas = 1
print(f'PARABÉNS! VOCÊ ACERTOU! VOCÊ UTILIZOU DE {tentativas} TENTATIVA(S)')
