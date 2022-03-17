# Exercício 060

n = int(input('Digite um número para saber seu fatorial: '))
inicial = n
fat = n
while n > 1:
    fat = fat * (n - 1)
    n -= 1
print(f'O fatorial de {inicial}! vale {fat}')

# Outra opção, mas com FOR

'''n = int(input('Digite um número para saber seu fatorial: ')) 
inicial = n  
fat = n  
for n in range (n,1,-1): 
    fat = fat*(n-1)  
print(f'O fatorial de {inicial}! vale {fat}')'''

'''existe a opção de importar a função factorial, que calcula o fatorial automaticamente com
from math import factorial'''