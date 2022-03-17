# Exercício 070

print(f'{"LISTA DE COMPRAS":=^40}\n')
tot_compra = m_mil = barato = 0
n_barato = ' '
while True:
    nome = str(input('Nome do produto: '))
    preco = float(input('Valor: R$ '))
    tot_compra += preco
    if preco > 1000:
        m_mil += 1
    if preco < barato or barato == 0:
        barato = preco
        n_barato = nome
    print('-' * 20)
    n = ' '
    while n not in 'SN':
        n = str(input('Quer continuar ? [S/N] ')).strip().upper()[0]
    print('-' * 20)
    if n == 'N':
        break
print(f'{"FIM DA COMPRA":=^40}')
print(f'O total da compra foi de R$ {tot_compra:.2f}')
print(f'{m_mil} produtos foram acima de R$ 1000.00')
print(f'O produto mais barato foi o {n_barato} que custa R$ {barato:.2f}')