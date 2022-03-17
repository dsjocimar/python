# Exercício 031

dist = float(input('Digite a distância da viagem em Km: ')) 
print(f'Você está prestes a viajar \033[1;33m{dist} km\033[m')
if dist <= 200:
    valor = dist * 0.5
    print(f'O valor da viagem é de \033[1;32mR$ {valor:.2f} reais\033[m')
else:
    valor = dist * 0.45
    print(f'O valor da viagem é de \033[1;32mR$ {valor:.2f} reais\033[m')