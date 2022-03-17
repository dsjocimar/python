# Exercício 082

num = list()
par = list()
impar = list()
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
for n in num:
    if n % 2 == 0:
        par.append(n)
    else:
        impar.append(n)
num.sort()
par.sort()
impar.sort()
print(f'A lista digitada foi {num}')
print(f'A lista dos pares é {par}')
print(f'A lista dos impares é {impar}')
