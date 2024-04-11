"""
11. Palabra enmascarada

Desarrollar un programa que permita ingresar una palabra por teclado y la devuelva 
enmascarada, mostrando la primer letra y la ultima, pero reemplazando 
los caracteres intermedios por asteriscos. 

Por ejemplo: si se ingresa la palabra “verde” se debe obtener “v***e”.
"""

palabra = input('Ingrese una palabra: ')
censura = len(palabra[1:-1])*'*'
palabra_censurada = palabra[0]+censura+palabra[-1]
print(palabra_censurada)