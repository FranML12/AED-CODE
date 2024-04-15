"""
12. Cartas de Truco

Desarrollar un programa que genere al azar tres cartas simulando una mano de truco. 
A continuacion debera:

   1) Informar si entre las cartas se encuentra el as de espadas

   2) Verificar si las tres cartas son del mismo palo. Si es asi, 
   identificar cual fue la mayor carta. En caso contrario, informarlo.
"""
import random

# Tenemos en cuenta que en el truco, no se utilizan los 8, 9 y 10.

# Generar tres números al azar del 1 al 12 (excluyendo 8, 9 y 10)
cartas = random.sample((1, 2, 3, 4, 5, 6, 7, 11, 12), 3)
palo = random.sample(('espadas', 'bastos', 'oros', 'copas'), 3)

# Mano es una tupla que contiene 3 tuplas (cada una con un numero y palo)
mano = tuple(zip(cartas, palo))

if (1, 'espadas') in mano:
    print("Entre las cartas se encuentra el as de espadas.")
else:
    print("Entre las cartas no se encuentra el as de espadas.")

# Verificar si las tres cartas son del mismo palo
if palo.count(palo[0]) == 3:
    print(f"Las tres cartas son del mismo palo: {palo[0]}")
    # En este caso tomamos la carta de numero mayor, no la jerarquia del truco.
    print(f"La mayor carta es: {max(cartas)}")
else:
    print("Las tres cartas no son del mismo palo.")

# Sin in:

"""
if mano[0] == ((1, 'espadas') or mano[1] == (1, 'espadas') or mano[2] == (1, 'espadas')):
    print("Entre las cartas se encuentra el as de espadas.")
else:
    print("Entre las cartas no se encuentra el as de espadas.")
"""

# Sin count 

"""
if palo[0] == palo[1] == palo[2]:
    print(f"Las tres cartas son del mismo palo: {palo[0]}")
    print(f"La mayor carta es: {max(cartas)}")
else:
    print("Las tres cartas no son del mismo palo.")
"""

# Sin zip:

"""
carta1 = random.randint(1, 12)
carta2 = random.randint(1, 12)
carta3 = random.randint(1, 12)
palo1 = random.choice(('espadas', 'bastos', 'oros', 'copas'))
palo2 = random.choice(('espadas', 'bastos', 'oros', 'copas'))
palo3 = random.choice(('espadas', 'bastos', 'oros', 'copas'))

if carta1 == 1 and palo1 == 'espadas' or carta2 == 1 and palo2 == 'espadas' or carta3 == 1 and palo3 == 'espadas':
    print("Entre las cartas se encuentra el as de espadas.")
else:
    print("Entre las cartas no se encuentra el as de espadas.")

if palo1 == palo2 == palo3:
    print(f"Las tres cartas son del mismo palo: {palo1}")
    print(f"La mayor carta es: {max(carta1, carta2, carta3)}")
else:
    print("Las tres cartas no son del mismo palo.")
"""
