# Exercício 029

vel = int(input('Qual a velocidade do carro? '))
if vel > 80:
    multa = 7 * (vel - 80)
    print(f'''Você recebeu uma multa de R$ {multa} reais por estar acima de  
80 km/h!''')
else:
    print('''Você está dentro dos padrões de velocidade! Dirija com segurança! 
Tenha um bom dia!''')
