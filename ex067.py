# Exercício 067

while True:
    print('=' * 40)
    n = int(input('Quer saber a tabuada de qual valor? '))
    print('=' * 40)
    c = 0
    if n < 0:
        break
    else:
        while c <= 10:
            print(f'{n} X {c} = {n * c}')
            c += 1
print('SAINDO...')