"""
8. Lanzamiento de dados

Simular un juego en el que se lanzan dos dados.

 Si ambos dados son iguales o la suma entre ellos es impar, 
 gana el usuario. En caso contrario, gana la maquina.
"""

import random

dado1 = random.randint(1, 6)
dado2 = random.randint(1, 6)

if dado1 == dado2 or (dado1 + dado2) % 2 != 0:
    print("¡Ganaste!")
else:
    print("¡Perdiste!")