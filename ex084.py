# Exercício 084

pessoa = list()
dado = list()
maior = menor = 0
while True:
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Peso: ')))
    if len(pessoa) == 0:
        maior = menor = dado[1]
    else:
        if dado[1] > maior:
            maior = dado[1]
        if dado[1] < menor:
            menor = dado[1]
    pessoa.append(dado[:])
    dado.clear()
    r = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    while r not in 'SN':
        r = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if r == 'N':
        break
    print()
print('=-' * 40)
print(f'No total foram adicionadas {len(pessoa)} pessoas')
print(f'O maior peso foi o de {maior} Kg. Peso de ', end='')
for p in pessoa:
    if p[1] == maior:
        print(f'{p[0]} ', end='')
print()
print(f'O menor peso foi o de {menor} Kg. Peso de ', end='')
for p in pessoa:
    if p[1] == menor:
        print(f'{p[0]} ', end='')
