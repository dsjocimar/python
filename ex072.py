# Exercício 072

numeros = ('zero', 'um', 'dois', 'três', 'quatro',
           'cinco', 'seis', 'sete', 'oito', 'nove',
           'dez', 'onze', 'doze', 'treze', 'quatorze',
           'quinze', 'dezesseis', 'dezessete', 'dezoito',
           'dezenove', 'vinte')
while True:
    seletor = int(input('Digite um valor entre 0 a 20: '))
    if 0 <= seletor <= 20:
        print(f'Você digitou o número {numeros[seletor]}')
        while True:
            n = str(input('Quer continuar? [S/N]')).strip().upper()[0]
            if n not in 'SN':
                print('Tente Novamente.', end=' ')
            else:
                break
        if n == 'N':
            break
    else:
        print('Tente Novamente.', end=' ')
