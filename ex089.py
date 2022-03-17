# Exercício 089

notas = list()
while True:
    nome = str(input('Nome: '))
    notas.append(nome)
    n1 = float(input('Nota 1: '))
    notas.append(n1)
    n2 = float(input('Nota 2: '))
    notas.append(n2)
    media = (n1 + n2) / 2
    notas.append(media)
    boletim.append(notas[:])
    notas.clear()
    r = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    while r not in 'SN':
        r = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if r == 'N':
        break
print('-=' * 30)
print(f'{"Nº":<5}{"NOME":<25}{"MÉDIA":<10}')
print('-' * 40)
for i, a in enumerate(boletim):
    print(f'{i:<4}{a[0]:<25}{a[2]:<20.1f}')
print('-' * 40)
while True:
    n = int(input('Mostrar notas de qual aluno? (999 interrompe) '))
    if n == 999:
        break
    elif n <= len(boletim) - 1:
        print(f'As notas do aluno {boletim[n][0]} são {boletim[n][1]} e {boletim[n][2]}')
    print('-' * 40)
print('FINALIZANDO...')
print(f'{"VOLTE SEMPRE!":-^30}')