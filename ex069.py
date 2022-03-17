# Exercício 069

maioridade = homem = m_menor = 0
while True:
    print('-' * 29)
    print(f'{"CADASTRE UMA PESSOA":^30}')
    print('-' * 29)
    idade = int(input('Digite a sua idade: '))
    if idade > 18:
        maioridade += 1
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Digite o seu sexo: [M/F] ')).strip().upper()[0]
    if sexo in 'Mm':
        homem += 1
    elif sexo in 'Ff' and idade < 20:
        m_menor += 1
    print('-' * 29)
    n = ' '
    while n not in 'SN':
        n = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if n == 'N':
        break
print(f'{"FIM DO PROGRAMA":=^31}')
print(f'Foram cadastrados {maioridade} pessoas com mais de 18 anos!')
print(f'Foram cadastrados {homem} homens.')
print(f'Foram cadastradas {m_menor} mulheres com menos de 20 anos!')

