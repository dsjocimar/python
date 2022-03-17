# Exercício 064

soma = 0
n = int(input('Leia um número inteiro. Digite 999 para parar '))
while n!= 999:
    soma += n 
    n = int(input('Leia um número inteiro. Digite 999 para parar '))
print(f'A soma total foi {soma}')