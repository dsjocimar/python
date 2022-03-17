# Exercício 055

maior = 0
menor = 0
for c in range(1, 6):
    print(f'Digite o peso da {c}ª pessoa: ')
    peso = float(input())
    if peso > maior:
        maior = peso
    if peso < menor or menor == 0:
        menor = peso
print(f'O maior peso lido foi {maior} Kg e o menor peso lido foi {menor} Kg')