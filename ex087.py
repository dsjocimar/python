# Exercício 087


par = s3 = maior = 0
numeros = [[], [], []]
for c in range(0, 3):
    for d in range(0, 3):
        n = int(input(f'Digite o valor {c},{d}: '))
        numeros[c].append(n)
        if n % 2 == 0:
            par += n
        if d == 2:
            s3 += n
        if c == 2:
            if n > maior:
                maior = n
print('=-' * 10)
print('NÚMEROS EM MATRIZ:')
for c in range(0, 3):
    for d in range(0, 3):
        print(f'{numeros[c][d]:^5}', end='')
    print()
print(f'A soma dos valores pares é {par};')
print(f'A soma dos valores da terceira coluna vale {s3};')
print(f'O maior valor da segunda linha é o {maior}')
