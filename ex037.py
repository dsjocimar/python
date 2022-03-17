# Exercício 037

num = int(input('Digite um número inteiro qualquer: '))
n = int(input('''Escolha qual a base decimal para conversão: 
1 - Binário; 
2 - Octal; 
3 - Hexadecimal\n'''))
if n == 1:
    print(bin(num)[2:])
elif n == 2:
    print(oct(num)[2:])
elif n == 3:
    print(hex(num)[2:])
else:
    print('OPÇÃO INVÁLIDA!')
