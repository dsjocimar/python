# Exercício 030

n = int(input('Digite um número: '))
if n % 2 == 0:
    print(f'O número \033[31m{n}\033[m é \033[1;32mPAR\033[m!')
else: 
    print(f'O número \033[31m{n}\033[m é \033[1;33mÍMPAR\033[m!')