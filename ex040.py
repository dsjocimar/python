# Exercício 040

n1 = float(input('Entre com a primeira nota: '))
n2 = float(input('Entre com a segunda nota: '))
media = (n1 + n2) / 2
print(f'Tirando {n1} e {n2}, a sua média é {media} ')
if media < 5:
    print('\033[1;31mREPROVADO!\033[m')
elif 5 < media <= 6.9:
    print('\033[1;33mRECUPERAÇÃO\033[m')
else:
    print('\033[1;32mAPROVADO\033[m')
