"""
11. Galeria de arte

Una galeria de arte desea preparar un catalogo de sus cuadros mas famosos.

Se realiza una prueba con tres cuadros y por cada uno se ingresa el ano en que fue creado.

El programa debera:

    Verificar si todos los cuadros son anteriores al siglo XX (El siglo XX es el siglo 
    pasado. Se inicio en el ano 1901 y termino en el ano 2000).
    
    Determinar si alguna de las obras fue creada en un ano que se ingresa por teclado.
    
    Informar la diferencia en anos entre la obra mas nueva y la mas antigua.
"""

""" 
Determinar si alguna de las obras fue creada en un ano que se ingresa por teclado.

No se si hubo una malinterpretacin mia o si el enunciado no es claro,
pero no se si se refiere a que se ingrese un año y se determine si alguna de las 
obras fue creada en ese año (lo cual no tiene sentido) puesto a que yo soy quien
ingresa los años. O quiere que las obras y sus años esten previamente declaradas 
y compruebe que lo ingresado por teclado sea igual a las fechas previamente declaradas.
"""

cuadro1 = int(input("Ingrese el año en que fue creado el primer cuadro: "))
cuadro2 = int(input("Ingrese el año en que fue creado el segundo cuadro: "))
cuadro3 = int(input("Ingrese el año en que fue creado el tercer cuadro: "))
siglo_XX = range(1901, 2001)

nueva = max(cuadro1, cuadro2, cuadro3)
antigua = min(cuadro1, cuadro2, cuadro3)
diferencia = nueva - antigua

if cuadro1 in siglo_XX and cuadro2 in siglo_XX and cuadro3 in siglo_XX:
    print(f"Todos los cuadros son anteriores al siglo XX. Y la diferencia entre la obra más nueva y la más antigua es de {diferencia} años.")
else:
    print(f"No todos los cuadros son anteriores al siglo XX. Y la diferencia entre la obra más nueva y la más antigua es de {diferencia} años.")

# Sin in:

""" 
if cuadro1 >= 1901 and cuadro1 <= 2000 and cuadro2 >= 1901 and cuadro2 <= 2000 and cuadro3 >= 1901 and cuadro3 <= 2000:
    print(f"Todos los cuadros son anteriores al siglo XX. Y la diferencia entre la obra más nueva y la más antigua es de {diferencia} años.")
else:
    print(f"No todos los cuadros son anteriores al siglo XX. Y la diferencia entre la obra más nueva y la más antigua es de {diferencia} años.") 
"""