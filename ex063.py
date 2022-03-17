# Exercício 063

n = int(input('Digite um número para saber até onde a sequencia de fibo vai: '))
c = 0
c1 = 1
c2 = 0
cont = 0
while cont < n:
    print(c1,end = ' >> ')
    c = c1+c2
    c2 = c1
    c1 = c
    cont+=1
print('ACABOU!')