# Exercício 093

jogador = dict()
gols = list()
soma = 0
jogador['nome'] = str(input('Digite o nome do jogador: ')).title()
partidas = int(input(f'Quantas partidas o {jogador["nome"]} jogou? '))
for c in range(0, partidas):
    n = int(input(f'Quantos gols foram feitos na partida {c} ? '))
    gols.append(n)
    soma += n
jogador['gols'] = gols
jogador['total'] = soma
print('-='*30)
print(jogador)
print('-='*30)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('=-'*30)
print(f'O jogador {jogador["nome"]} jogou {partidas} partidas.')
for c in range(0, partidas):
    print(f'    - Na partida {c}, fez {gols[c]} gols.')
print(f'Foi um total de {soma} gols!')
