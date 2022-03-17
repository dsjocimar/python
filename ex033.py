# Exercício 033

n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))
if n1 > n2 and n1 > n3:
    if n2 > n3:
        print('O primeiro valor é o maior e o terceiro valor é o menor!')
    else:
        print('O primeiro valor é o maior e o segundo é o menor!')
else:
    if n2 > n1 and n2 > n3:
        if n1 > n3:
            print('O segundo valor é o maior e o terceiro é o menor!')
        else:
            print('O segundo valor é o maior e o primeiro é menor!')
    else:
        if n3 > n2 and n3 > n1:
            if n2 > n1:
                print('O terceiro valor é o maior e o primeiro é o menor!')
            else:
                print('O terceiro valor é o maior e o segundo é o menor!')
