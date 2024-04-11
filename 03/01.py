"""
1. Plazo fijo

Desarrollar un programa que cargue por teclado la cantidad de dinero depositada 
en plazo fijo por un cliente de un banco y calcular el saldo que tendra esa 
cuenta al vencer el plazo fijo, sabiendo que el interes pactado era de 2.3% 
y que el banco cobra una tasa fija de gastos por servicios financieros igual $20 por cuenta.
"""
monto_inicial = int(input('Ingrese el dinero depositado: '))
interes_por_mes = 0.023  # 2.3%
meses = int(input('Ingrese la cantidad de meses: '))

saldo = (monto_inicial * (1 + interes_por_mes) ** meses)-20

print("El saldo después de", meses, "meses es:", saldo)