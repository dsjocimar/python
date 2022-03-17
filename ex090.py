# Exercício 090

boletim = dict()
boletim['Nome'] = str(input('Nome: '))
boletim['Media'] = float(input(f'Média de {boletim["Nome"]}: '))
if boletim['Media'] >= 7:
    boletim['Situaçao'] = 'Aprovado'
else:
    boletim['Situaçao'] = 'Reprovado'
for k, v in boletim.items():
    print(f'{k} é igual a {v}')

