# Exercício 056

idade_total = 0
maior_homem = 0
tot_mulher = 0
for c in range(1, 5):
    print(f'-------{c}ª PESSOA-------')
    nome = str(input('Digite o seu nome: '))
    idade = int(input('Digite a sua idade: '))
    sexo = str(input('Qual o seu sexo: H/h: homem // M/m: mulher '))
    idade_total += idade
    if sexo in 'Hh' and idade > maior_homem:
        maior_homem = idade
        homem_mais_velho = nome
    if sexo in 'Mm' and idade < 20:
        tot_mulher += 1
media = idade_total / 4
print(f'A média da idade das pessoas é {media:.2f}')
print(f'O homem mais velho é o {homem_mais_velho}, com {maior_homem} anos')
print(f'O total de mulheres que tem menos de 20 anos é {tot_mulher}')
