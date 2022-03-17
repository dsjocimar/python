# Exercício 027
nome = str(input('Digite seu nome completo: ')).strip()
divisao = nome.split()
print('Muito prazer em te conhecer!')
print(f'Seu primeiro nome é {divisao[0]}')
print(f'Seu último nome é {divisao[len(divisao) - 1]}')
