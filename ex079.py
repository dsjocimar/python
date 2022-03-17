# Exercício 079

n = list()
while True:
    num = int(input('Digite um valor: '))
    if num not in n:
        n.append(num)
        print('Número adicionado com sucesso!')
    else:
        print('Valor DUPLICADO! Digite novamente!')
    cont = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    while cont not in 'SN':
        cont = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if cont == 'N':
        break
n.sort()
print('=-'*30)
print(f'Você digitou os valores \033[1m{n}\033[m')
