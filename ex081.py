# Exercício 081

num = list()
total = 0
while True:
    num.append(int(input('Digite um valor: ')))
    total += 1
    r = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    while r not in 'SN':
        r = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if r == 'N':
        break
print('-=' * 20)
print(f'O total de números digitados foi {total}')
print(f'Lista decrescente: ', end='')
num.sort(reverse=True)

# Outra opção:

'''for c in range (total,0,-1): 
    print(num[c-1],end=' ')'''
print(num)
if 5 in num:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 não faz parte da lista!')