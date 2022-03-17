# Exercício 032

from datetime import date

ano = int(input('Digite um ano qualquer. Digite 0 para analisar o ano ATUAL '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'O ano de \033[1m{ano}\033[m \033[1;32mé BISSEXTO!\033[m')
else:
    print(f'O Ano de \033[1m{ano}\033[m \033[1;32mNÃO BISSEXTO!\033[m')
