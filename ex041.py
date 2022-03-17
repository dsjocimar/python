# Exercício 041

from datetime import date
print('\033[1;34m=\033[m'*32)
print('\033[1;34mCONFEDERAÇÃO NACIONAL DE NATAÇÃO\033[m')
print('\033[1;34m=\033[m' * 32)
print('Vamos verificar a sua categoria...')
ano = int(input('Digite o seu ano de nascimento: '))
dif = date.today().year - ano
print(f'Você possui {dif} anos')
if dif <= 9:
    print('\033[1;32mCATEGORIA MIRIM!\033[m')
elif 9 < dif <= 14:
    print('\033[1;33mCATEGORIA INFANTIL!\033[m')
elif 14 < dif <= 19:
    print('\033[1;34mCATEGORIA JÚNIOR!\033[m')
elif 19 < dif <= 25:
    print('\033[1;35mCATEGORIA SÊNIOR!\033[m')
else:
    print('\033[1;36mCATEGORIA MASTER!\033[m')


