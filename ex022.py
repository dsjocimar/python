# Exercício 022

nome = str(input('Digite o seu nome: ')).strip()
print('Analisando o seu nome...')
'''Realizar a impressão na tela do nome em maiúsculas'''
print(f'O seu nome em letras maíusculas é {nome.upper()};')
'''Realizar a impressão na tela do nome em minúsculas'''
print(f'O seu nome em letras minúsculas é {nome.lower()};')
'''Mostrar a quantidade de letras que o nome possui sem espaços'''
print(f'A quantidade de letras do nome sem os espaços é {len(nome) - nome.count(" ")}')
'''Contar quantas letras tem o primeiro nome'''
solto = nome.split()
print(f'A quantidade de letras no primeiro nome é {len(solto[0])}')
'''Outra opção para achar a ultima palavra do nome é
print(f'Seu primeiro nome tem {(nome.find(" "))}')'''