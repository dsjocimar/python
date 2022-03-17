# Exercício 054

from datetime import date
hoje = date.today().year
maior = 0
menor = 0
for c in range(1, 8):
    ano = int(input(f'Digite o seu ano de nascimento da {c}ª pessoa: '))
    if hoje - ano < 21:
        menor += 1
    else:
        maior += 1
print(f'Existem {maior} pessoas que já atingiram a maioridade!')
print(f'Existem {menor} pessoas que ainda não atingiram a maioridade!')