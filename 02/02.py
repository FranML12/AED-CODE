"""
2. Descuento en medicinas

Calcular el descuento y el monto a pagar por un medicamento cualquiera en una farmacia
(cargar por teclado el precio de ese medicamento) sabiendo que todos los medicamentos tienen un descuento del 35%. 
Mostrar el precio actual, el monto del descuento y el monto final a pagar.
"""

# descuento = 65 ya que al aplicar la regla de 3 se necesita el % del precio final (100-35=65)
descuento = 65
producto = float(input('Ingrese el precio del producto'))

# Se aplica regla de 3
descontado = descuento * (producto/100)

print(descontado)