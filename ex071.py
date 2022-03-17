# Exercício 071

'''print(f'{"BANCO FULANO DE TAL":=^40}')
print('BOM DIA!')
valor = int(input('DESEJA SACAR QUAL VALOR? R$ '))
tot_50 = tot_20 = tot_10 = tot_1 = 0
while valor > 0:
    if valor % 50 == 0:
        tot_50 +=1
        valor -=50
    elif valor % 20 == 0:
        tot_20 += 1
        valor -= 20
    elif valor % 10 == 0:
        tot_10 += 1
        valor -= 10
    else:
        tot_1 += 1
        valor -= 1
print ('='*40)
if tot_50 > 0:
    print(f'Total de {tot_50} cédulas de R$ 50')
if tot_20 > 0:
    print(f'Total de {tot_20} cédulas de R$ 20')
if tot_10 > 0:
    print(f'Total de {tot_10} cédulas de R$ 10')
if tot_1 > 0:
    print(f'Total de {tot_1} cédulas de R$ 1')
print('='*40)
print('SEJA BEM VINDO AO BANCO FULANO DE TAL! TENHA UM BOM DIA!')'''

# Outra opção para o programa...

print(f'{"BANCO FULANO DE TAL":=^40}')
print('BOM DIA!')
valor = int(input('DESEJA SACAR QUAL VALOR? R$ '))
total = valor
ced = 50
totced = 0
while True:
    if total >= ced:
        total -= ced
        totced += 1
    else:
        if totced > 0:
            print(f'Total de {totced} cédulas de R$ {ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totced = 0
        if total == 0:
            break
print('=' * 40)
print('SEJA BEM VINDO AO BANCO FULANO DE TAL! TENHA UM BOM DIA!')