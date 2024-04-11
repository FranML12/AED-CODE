"""
9. Datos de un rectangulo

Hacer un programa que tome como entrada el ancho y el alto de un rectangulo y 
determine el perimetro y la superficie del mismo.
"""

largo = float(input('Ingrese el largo del rectangulo: '))
ancho = float(input('Ingrese el ancho del rectangulo: '))

perimetro = largo*2+ancho*2
superficie = largo*ancho

print(f'El perimetro es: {perimetro}, la superficie: {superficie}')