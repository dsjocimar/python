# Exercício 035

r1 = int(input('Digite o valor da primeira reta: '))
r2 = int(input('Digite o valor da segunda reta: '))
r3 = int(input('Digite o valor da terceira reta: '))
if r1 + r2 > r3 and r1 + r3 > r2 and r2 + r3 > r1:
    print('\033[1;36mÉ possivel formar um triângulo!\033[m')
else:
    print('\033[1;31mNão é possivel formar um triângulo!\033[m')
