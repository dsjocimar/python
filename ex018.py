# Exercício 018
from math import sin, cos, tan, radians
n = float(input('Digite o ângulo que você deseja:\n'))
seno = sin(radians(n))
cosseno = cos(radians(n))
tangente = tan(radians(n))
print(f'O SENO do ângulo de {n} vale {seno:.2f};\n'
      f'O COSSENO do ângulo de {n} vale {cosseno:.2f};\n'
      f'A TANGENTE do ângulo de {n} vale {tangente:.2f}')
