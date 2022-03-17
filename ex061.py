# Exercício 061

n = int(input('Digite o primeiro termo da P.A: '))
r = int(input('Digite a razão da P.A: '))
c = 1
while c <= 10:
    print((n + ((c - 1) * r)), end=' >> ')
    c += 1
print('ACABOU!')
