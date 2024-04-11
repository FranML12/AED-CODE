"""
8. Rinde de un Campo Agricola

Un productor agricola desea saber cuantos quintales de trigo puede producir en su parcela. 
Se pide ingresar el largo y el ancho en metros de la parcela y 
determinar el rinde sabiendo que en 10 m2 se obtienen 2 quintal
"""

largo = float(input('Ingrese el largo: '))
ancho = float(input('Ingrese el ancho: '))

parcela = largo*ancho # Area de la parcela (m2)
quintales = parcela/5 # Calcula la cantidad de quintales (cada 10m2 = 2 entonces 5m2 = 1)

print(f'En la parcela se pueden pruducir {quintales} quintales.')