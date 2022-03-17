# Exercício 036

print('=-' * 20)
print('          \033[1;32mBANCO FULANO DE TAL\033[m')
print('=-' * 20)
print('BOM DIA!')
casa = float(input('Digite o valor do imóvel solicitado R$ '))
salario = float(input('Digite o valor do seu salário R$ '))
tempo = int(input('Em quanto tempo em anos que pretende pagar o empréstimo solicitado? '))
emprestimo = casa / (tempo*12)
parcela = salario * 0.3
if emprestimo > parcela:
    print('\033[1;31mEMPRÉSTIMO NEGADO!\033[m')
else:
    print('\033[1;33mEMPRÉSTIMO ACEITO!\033[m')
print(f'O valor referente ao seu empréstimo solicitado será de R$ {emprestimo:.2f}')
