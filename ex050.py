# Exercício 050

soma = 0
for c in range(1, 7):
    print('Leia o', c, 'o. número inteiro: ')
    n = int(input())
    if n % 2 == 0:
        soma += n
print(f'A soma dos números que são pares é {soma}')