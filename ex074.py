# Exercício 074

from random import randint

aleatorio = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10),
             randint(1, 10))
print(f'A lista de números aleatório foi {aleatorio}')
maior = menor = aleatorio[0]
for n in range(0, len(aleatorio)):
    if aleatorio[n] > maior:
        maior = aleatorio[n]
    if aleatorio[n] < menor:
        menor = aleatorio[n]
print(f'O maior valor da tupla é o {maior} e o menor é o {menor}')

# Existe também a opção de fazer com método
print(f'O maior valor da tupla é o {max(aleatorio)} e o menor é o {min(aleatorio)}')

