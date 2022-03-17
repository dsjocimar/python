# Exercício 043

print('\033[32m*\033[m' * 20)
print('   \033[32mCALCULO DE IMC\033[m')
print('\033[32m*\033[m' * 20)

peso = float(input('Digite o seu peso (Kg): '))
h = float(input('Digite a sua altura (mt): '))
imc = peso / h ** 2
print(f'O seu IMC é de {imc:.1f}')
if imc < 18.5:
    print('\033[1mABAIXO DO PESO!\033[m')
elif 18.5 < imc <=25:
    print('\033[1mPESO IDEAL!\033[m')
elif 25 < imc <=30:
    print('\033[1mSOBREPESO\033[m')
elif 30 < imc <= 40:
    print('\033[1mOBESIDADE\033[m')
else:
    print('\033[1mOBESIDADE MÓRBIDA\033[m')

