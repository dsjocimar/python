# Exercício 062

n = int(input('Digite o primeiro termo da P.A: '))
r = int(input('Digite a razão da P.A: '))
c = 1
cont = 10
while cont != 0:
    while c <= cont:
        print((n + ((c - 1) * r)), end=' >> ')
        c += 1
    print('PAUSA!\n')
    cont = int(input('Deseja saber mais quantos números? Digite 0 para sair: '))
    if cont != 0:
        cont = (c - 1) + cont
print('ACABOU!')