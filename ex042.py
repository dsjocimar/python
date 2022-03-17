# Exercício 042

r1 = float(input('Digite o primeiro lado do triângulo: '))
r2 = float(input('Digite o segundo lado do triângulo: '))
r3 = float(input('Digite o terceiro lado do triângulo: '))
if r1 + r2 > r3 and r1 + r3 > r2 and r2 + r3 > r1:
    print('\033[1;35mÉ possível formar um \033[m', end='')
    if r1 == r2 == r3:
        print('\033[1;32mTRIANGULO EQUILÁTERO!\033[m')
    elif r1 == r2 or r1 == r3 or r2 == r3:
        print('\033[1;33mTRIÂNGULO ISOSCELES!\033[m')
    else:
        print('\033[1;34mTRIÂNGULO ESCALENO!\033[m')
else:
    print('\033[1;31mNÃO é possivel formar um triângulo\033[m')
