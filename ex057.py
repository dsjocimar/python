# Exercício 057

sexo = str(input('Digite o seu sexo [M/F] ')).strip().upper()[0]
while sexo not in 'MF':
    sexo = str(input('Dados incorretos! Digite o seu sexo [M/F] ')).strip().upper()[0]
print('fim')
