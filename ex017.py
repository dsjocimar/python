'''Solução sem a importação de classes
cat_op = float(input('Qual o comprimento do cateto oposto:\n'))
cat_ad = float(input('Qual o comprimento do cateto adjacente:\n'))
hipotenusa = ((cat_op**2 + cat_ad**2)**(1/2))
print (f'A hipotenusa vai medir {hipotenusa:.2f}')'''

'''Importação da classe math'''
from math import hypot
cat_op = float(input('Qual o comprimento do cateto oposto: '))
cat_ad = float(input('Qual o comprimento do cateto adjacente: '))
hipotenusa = hypot(cat_op, cat_ad)
print(f'A hipotenusa vai medir {hipotenusa:.2f}')
