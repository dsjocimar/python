# Exercício 034

sal = float(input('Digite qual o seu salário: R$ '))
if sal > 1250:
    print(f'O seu novo salário será \033[1;34mR$ {sal + (sal * 0.1):.2f}\033[m')
else:
    print(f'O seu novo salário será \033[1;35mR$ {sal + (sal * 0.15):.2f}\033[m')
