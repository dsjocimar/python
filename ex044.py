# Exercício 044

'''Para escrever uma string formatada o método é esse abaixo'''

print('{:^40}'.format('Lojas da bahia'))        # método 1
print(f'{"Lojas da Bahia":^40}')             # método 2
preco = float(input('Digite o valor a ser pago pelo produto: R$ '))
n = int(input('''Digite o método de pagamento 
1 - Á vista/Cheque; 
2 - Á vista no cartão; 
3 - Em até 2x no cartão; 
4 - 3x ou mais no cartão\n'''))
if n == 1:
    preco = preco - (preco * 0.1)
elif n == 2:
    preco = preco - (preco * 0.05)
elif n == 3:
    parc = preco/2
    print(f'Sua compra vai ser dividida em 2 parcelas de R$ {parc:.2f}')
elif n == 4:
    parcelas = int(input('Em quantas parcelas vai dividir a compra? '))
    preco = preco + (preco * 0.2)
    p_final = preco / parcelas
    print(f'Sua compra vai ser dividida em {parcelas} parcelas de R$ {p_final:.2f} COM JUROS')
print(f'O valor a ser pago será R$ {preco:.2f}')

