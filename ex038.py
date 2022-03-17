# Exercício 038

n1 = float(input('Digite o primeiro valor: '))
n2 = float(input('Digite o segundo valor: '))
if n1 > n2:
    print('O \033[33mPRIMEIRO VALOR\033[m É \033[34mMAIOR!\033[m')
elif n1 < n2:
    print('O \033[33mSEGUNDO VALOR\033[m É O \033[34mMAIOR!\033[m')
else:
    print('\033[33mNÃO EXISTE\033[m VALOR MAIOR, OS DOIS SÃO \033[34mIGUAIS!\033[m')
