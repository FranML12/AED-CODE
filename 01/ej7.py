"""
7. Precio del boleto

Se desea conocer el precio de un boleto de viaje en omnibus de media distancia. 
Para el calculo del mismo se debe considerar el monto base (que se cobra siempre), 
mas un valor extra calculado en base a la cantidad de kilometros a recorrer:  
Por cada kilometro a recorrer se cobra $0.30 de adicional.
"""

base = 50
dist = float(input('Cuantos kilometros desea recorrer? '))
bol = base + dist*0.30

print(f'Precio del boleto: ${bol}')