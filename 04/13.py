"""
13. Calculo de Precios con Descuento

Una empresa nos solicito un programa que nos permita calcular los precios de los 
productos que vende al publico

para ello, nuestro programa debe pedir el precio unitario, la cantidad que se vendio 
y si se pago en efectivo o no.

En base a esto determinar

    1) El Precio final sin descuentos del articulo (precio unitario por cantidad)

    2) Calcular un descuento si el usuario pago en efectivo y la cantidad vendida es 
    superior a 10 unidades del 15% caso contrario solo aplicar un 5% de descuento
"""

precio_unitario = float(input("Ingrese el precio unitario: "))
cantidad = int(input("Ingrese la cantidad vendida: "))
pago_efectivo = input("¿Pago en efectivo? (si/no): ")

if pago_efectivo == "si" and cantidad > 10:
    precio_final = precio_unitario * cantidad * 0.85
    print(precio_final)
else:
    precio_final = precio_unitario * cantidad * 0.95
    print(precio_final)