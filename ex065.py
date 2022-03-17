# Exercício 065

c = 'S'
somatoria = 0
qtd = 0
media = 0
maior = menor = 0
while c in 'Ss':
    n = int(input('Digite um número inteiro: '))
    qtd += 1
    somatoria += n
    if n > maior:
        maior = n
    if n < menor or menor == 0:
        menor = n
    c = str(input('Quer continuar a digitar valores? [S/N] ')).upper().strip()[0]
media = somatoria / qtd
print(f'A média dos valores digitados foi {media:.2f}')
print(f'O maior valor digitado foi {maior} e o menor valor digitado foi {menor}')