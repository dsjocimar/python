# Exercício 039

from datetime import date
ano = int(input('Digite o ano do seu nascimento: '))
dif = date.today().year - ano
if dif < 18:
    temp_restante = 18 - dif
    alistamento = date.today().year + temp_restante
    print(
        f'Ainda está cedo para se alistar ao exército! Ainda faltam \033[32m{temp_restante} anos\033[m para se alistar!')
    print(f'Seu alistamento será em {alistamento}')
elif dif == 18:
    print('\033[1mEstá na hora de se alistar ao exército!\033[m')
else:
    temp_passado = dif - 18
    alistamento = date.today().year - temp_passado
    print(f'Já passou do tempo de se alistar ao exército! Já se passaram \033[31m{temp_passado} anos\033[m do seu '
          f'alistamento!')
    print(f'Você deveria ter se alistado em {alistamento}')
