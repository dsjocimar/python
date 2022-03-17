# Exercício 051

n = int(input('Digite o primeiro termo da P.A: '))
r = int(input('Digite a razão da P.A: '))
print('Os 10 primeiros termos dessa P.A serão:')
for c in range(1, 11):
    print((n + (c - 1) * r),end=' >> ')
print('ACABOU!')
