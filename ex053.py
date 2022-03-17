# Exercício 053

frase = str(input('Digite uma frase: ')).strip().upper()
separada = frase.split()
junto = ''.join(separada)
inverso = ''
for c in range(len(junto) - 1, -1, -1):
    inverso += junto[c]
print(f'O inverso de {junto} é {inverso}')
if inverso == junto:
    print('O nome escrito É um palindromo')
else:
    print('O nome escrito NÃO é um palindromo!')
'''Um macete seria substituir o for pelo seguinte programa
inverso = junto[::-1]'''
