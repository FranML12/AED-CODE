"""
5. Conversion de medidas

Desarrolle un programa para convertir una medida dada en pies a sus equivalentes en: 

            yardas 
            pulgadas 
            centimetros 
            metros 

Sabiendo que: 1 pie = 12 pulgadas, 1 yarda = 3 pies,  1 pulgada = 2.54 centimetros, 1 metro = 100 centimetros.
"""

userPie = float(input('Ingrese la medida en pies: '))

pul = userPie * 12
yar = userPie/3
cm = pul*2.54
mt = cm/100

print(f'Medida convertida:\nyardas: {yar}\npulgadas: {pul}\ncentimetros: {cm}\nmetros: {mt}')