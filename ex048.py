# Exercício 048

"""soma = 0
for n in range (1,501):
    if n % 2 != 0 and n % 3 == 0:
        soma += n
print(f'''A soma entre todos os números impares entre 1 até 500 e que são
múltiplos de 3 é {soma}''')"""
# Outra forma de calcular, utilizando menos a memória
soma = 0
cont = 0
for n in range(1, 501, 2):
    if n % 3 == 0:
        soma += n
        cont += 1
print(f'''A soma entre todos os {cont} números impares entre 1 até 500 e que são   
múltiplos de 3 é {soma}''')