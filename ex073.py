# Exercício 73

tabela = ('Atlético Mineiro', 'Flamengo', 'Palmeiras', 'Fortaleza', 'Corinthians', 'Bragantino', 'Fluminense',
          'América Mineiro', 'Atlético Goianiense', 'Santos', 'Ceará', 'Internacional', 'São Paulo',
          'Atlético Paranaense', 'Cuiabá', 'Juventude', 'Grêmio', 'Bahia', 'Sport', 'Chapecoense')

print(f'{"BRASILEIRÃO 2021":=^40}')
print('Tabela de times e suas colocações:')
for pos, t in enumerate (tabela):
    print(f'{pos+1}º colocado: {t}')
print('=-' * 20)
print('Tabela dos primeiros 5 colocados:')
for c in range(0, 5):
    print(f'{c + 1}º colocado: {tabela[c]}')
print('=-' * 20)
print('Tabela dos últimos 4 colocados:')
for c in range(16, 20):
    print(f'{c + 1}º colocado: {tabela[c]}')
print('=-' * 20)
ordemalfa = sorted(tabela)
print('Ordem alfabética dos times do Brasileirão 2021:')
for c in range(0, 20):
    print(f'{c + 1} - {ordemalfa[c]}')
print('=-' * 20)
print(f'O Chapecoense está na {tabela.index("Chapecoense")+1}ª posição')
