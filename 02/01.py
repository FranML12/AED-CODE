"""
1. Cuadrados y cubos

Leer dos numeros y calcular:

        La suma de sus cuadrados.
        El promedio de sus cubos.
"""

n1 = float(input('Ingrese un numero'))
n2 = float(input('Ingrese otro numero'))

sumCuad = n1**2 + n2**2
promCub = (n1**3 + n2**3) / 2

print(sumCuad)
print(promCub)