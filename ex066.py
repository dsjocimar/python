# Exercício 066

soma = total = 0
while True:
    n = int(input('Digite um valor [999 para parar]: '))
    if n == 999:
        break
    soma += n
    total += 1
print(f'O total de números digitados foi {total} e a soma deles vale {soma}') 