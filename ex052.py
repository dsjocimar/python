# Exercício 052

div = 0
n = int(input('Digite um número: '))
for c in range(1, n + 1):
    if n % c == 0:
        div += 1
        print('\033[1;33m',end='')
    else:
        print('\033[1;31m',end='')
    print(f'{c}', end=' ')
print('\033[m')
if div <= 2:
    print(f'\nO número {n} É primo!')
else:
    print(f'\nO número {n} NÃO é primo! Ele foi divisível {div} vezes!')
