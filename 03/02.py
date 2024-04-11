"""
2. Fecha como cadena

Desarrollar un programa que cargue por teclado una cadena de caracteres que 
se supone representa una fecha en formato 'dd/mm/aaaa', y muestre por separado el dia, 
el mes y el ano. Ejemplo: si la cadena ingresada es '16/03/2016' el programa debe mostrar: 
'Dia: 16  -  Mes: 03  -  Ano: 2016'.
"""

fecha = input('Ingrese dd/mm/aaaa: ')
dia = fecha[:2]
mes = fecha[3:5]
ano = fecha[6:10]
print(f'Dia: {dia}  -  Mes: {mes}  -  Ano: {ano}')