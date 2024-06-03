data = open('envios.txt', 'rt') # Abro el archivo como lector en modo texto
data_line = data.readline() # Primera linea de txt
sig = True

def main():
    def read():
        global cp, direccion, tipo, pago
        data_line = data.readline() # Procesa el resto del texto
        # if data_line implicita el if data_line == True
        if data_line: # Un string siempre va a ser True
            """ 
            Declaramos variables necesarias leyendo el texto y especificamos que
            son variables globales para que funcionen en todo archivo py.
            Sobre pago: Se puede hacer con -1 pero evitamos posibles errores de 
            espacios o caracteres extra en el txt
            """
            cp = data_line[0:9]
            direccion = data_line[9:29]
            tipo = int(data_line[29])
            pago = int(data_line[30])
        else:
            global sig
            sig = False
    read()
    
    # Funcion para eliminar los espacios extra en el codigo
    def borrar_espacios(rango):
        resultado = ''
        for i in rango:
            if i != ' ':
                resultado += i
        return resultado
    
    global cp, direccion
    cp, direccion = borrar_espacios(cp), borrar_espacios(direccion)

    def info():
        # Determinar el destino en base al formato del cp
        def formato_cp(cp):
            def es_letra(c):
                return 'A' <= c <= 'Z' or 'a' <= c <= 'z'

            def es_digito(c):
                return '0' <= c <= '9'

            if len(cp) == 8 and es_letra(cp[0]) and all(es_digito(c) for c in cp[1:5]) and all(es_letra(c) for c in cp[5:]):
                return 'Argentina'
            elif len(cp) == 4 and all(es_digito(c) for c in cp):
                return 'Bolivia'
            elif len(cp) == 9 and all(es_digito(c) for c in cp[0:5]) and cp[5] == '-' and all(es_digito(c) for c in cp[6:]):
                return 'Brasil'
            elif len(cp) == 7 and all(es_digito(c) for c in cp):
                return 'Chile'
            elif len(cp) == 6 and all(es_digito(c) for c in cp):
                return 'Paraguay'
            elif len(cp) == 5 and all(es_digito(c) for c in cp):
                return 'Uruguay'
            else:
                return 'Formato desconocido'
        destino = formato_cp(cp)

        # Determinar el precio inicial
        def tipo_precio(tipo):
            if tipo == 0:
                precio = 1100
            elif tipo == 1:
                precio = 1800
            elif tipo == 2:
                precio = 2450
            elif tipo == 3:
                precio = 8300
            elif tipo == 4:
                precio = 10900
            elif tipo == 5:
                precio = 14300
            elif tipo == 6:
                precio = 17900
            else:
                precio = 0
                print("Tipo de envío inválido.")
            return precio
        precio = tipo_precio(tipo)

        # Calcular el precio inicial
        def precio_inicial():
            if destino == 'Argentina':
                inicial = precio
            elif destino == 'Bolivia' or destino == 'Paraguay':
                inicial = (precio * 0.20) + precio 
            elif destino == 'Uruguay':
                if cp[0] == '1':
                    inicial = (precio * 0.20) + precio
                else:
                    inicial = (precio * 0.25) + precio
            elif destino == 'Chile':
                inicial = (precio * 0.25) + precio
            elif destino == 'Brasil':
                if cp[0] == '8' or cp[0] == '9':
                    inicial = (precio * 0.20) + precio
                elif cp[0] == '4' or cp[0] == '5' or cp[0] == '6' or cp[0] == '7':
                    inicial = (precio * 0.30) + precio
                else:
                    inicial = (precio * 0.25) + precio
            else:
                inicial = (precio * 0.5) + precio
            return inicial
        inicial = precio_inicial()

        # Calcular el precio final
        def precio_final():
            if pago == 1:
                final = inicial - (inicial * 0.1)
            elif pago == 2:
                final = inicial
            else:
                final = 'Tipo de pago no admitido'
            return final
        final = precio_final()

        print("País de destino del envío:", destino)
        print("Importe inicial a pagar:", int(inicial))
        print("Importe final a pagar:", int(final)) 
    info()

while sig:
    main()

""" 
def results():
    print(' (r1) - Tipo de control de direcciones:', control)
    print(' (r2) - Cantidad de envios con direccion valida:', cedvalid)
    print(' (r3) - Cantidad de envios con direccion no valida:', cedinvalid)
    print(' (r4) - Total acumulado de importes finales:', imp_acu_total)
    print(' (r5) - Cantidad de cartas simples:', ccs)
    print(' (r6) - Cantidad de cartas certificadas:', ccc)
    print(' (r7) - Cantidad de cartas expresas:', cce)
    print(' (r8) - Tipo de carta con mayor cantidad de envios:', tipo_mayor)
    print(' (r9) - Codigo postal del primer envio del archivo:', primer_cp)
    print('(r10) - Cantidad de veces que entro ese primero:', cant_primer_cp)
    print('(r11) - Importe menor pagado por envios a Brasil:', menimp)
    print('(r12) - Codigo postal del envio a Brasil con importe menor:', mencp)
    print('(r13) - Porcentaje de envios al exterior sobre el total:', porc)
    print('(r14) - Importe final promedio de los envios a Buenos Aires:', prom) 
"""