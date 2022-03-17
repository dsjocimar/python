# Exercício 078

num = list()
for n in range(0, 5):
    num.append(int(input(f'Digite um valor para a posição {n}: ')))
maior = menor = 0
for n in num:
    if n > maior:
        maior = n
    if n < menor or menor == 0:
        menor = n
print('-='*20)
print(f'Você digitou os valores: {num}')
print(f'O maior valor digitado foi o {maior} nas posições ', end='')
for pos, n in enumerate(num):
    if maior == n:
        print(pos, end='...')

print(f'\nO menor valor digitado foi o {menor} nas posições ', end='')
for pos, n in enumerate(num):
    if menor == n:
        print(pos, end='...')

