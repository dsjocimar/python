# Exercício 075

n = (int(input('Digite o 1º valor: ')),
     int(input('Digite o 2º valor: ')),
     int(input('Digite o 3º valor: ')),
     int(input('Digite o 4º valor: ')))
print(f'Você digitou os valores {n}')
print(f'O valor 9 apareceu {n.count(9)} vezes;')
if 3 in n:
    print(f'O primeiro valor 3 apareceu na {n.index(3) + 1}ª posição;')
else:
    print('O valor 3 não foi digitado em nenhuma posição;')
print('Os números pares foram', end=' ')
for c in n:
    if c % 2 == 0:
        print(c, end=' ')
