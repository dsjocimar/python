# Exercício 086

numeros = [[], [], []]
for c in range(0, 3):
    for d in range(0, 3):
        n = int(input(f'Digite o valor {c},{d}: '))
        numeros[c].append(n)
print('=-' * 10)
print('NÚMEROS EM MATRIZ:')
for c in range(0, 3):
    for d in range(0, 3):
        print(f'{numeros[c][d]:^5}', end='')
    print()
