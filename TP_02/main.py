data = open('envios.txt', 'rt')  # Abro el archivo como lector en modo texto
data_line = data.readline()  # Primera linea de txt

sig = True
imp_acu_total = 0
cedinvalid, cedvalid = 0, 0
ccs, cce, ccc = 0, 0, 0
primer_cp = None
pcp = 0
cant_primer_cp = 0
menimp, antmenimp = 0, None
mencp = 0
count_env_exterior = 0
prom = 0
acc_arg_ba, count_arg_ba = 0, 0


def control():
    r1 = False
    if 'HC' in data_line:
        r1 = 'Hard Control'
    if 'SC' in data_line:
        r1 = 'Soft Control'
    return r1


control = control()

while sig:
    data_line = data.readline()  # Procesa el resto del texto
    # if data_line implicita el if data_line == True
    if not data_line:  # Un string siempre va a ser True
        sig = False
        break
    else:
        """ 
        Declaramos variables necesarias leyendo el texto y especificamos que
        son variables globales para que funcionen en todo archivo py.
        Sobre pago: Se puede hacer con -1 pero evitamos posibles errores de 
        espacios o caracteres extra en el txt
        """
        cp = data_line[:9]
        direccion = data_line[9:29]
        tipo = int(data_line[29])
        pago = int(data_line[30])


    # Funcion para eliminar los espacios extra en el codigo
    def borrar_espacios(rango):
        resultado = ''
        for i in rango:
            if i != ' ':
                resultado += i
        return resultado


    def es_letra(c):
        return 'A' <= c <= 'Z' or 'a' <= c <= 'z'


    def es_mayus(c):
        return 'A' <= c <= 'Z'


    def es_digito(c):
        return '0' <= c <= '9'


    direccion = borrar_espacios(direccion)


    # Direccion no soporta tildes. Solo mayuscula, minuscula, numeros enteros y puntos
    def direccion_hc():
        global direccion
        anterior = ''
        for i in direccion:
            if not es_letra(i) and not es_digito(i) and i != '.':
                direccion = 'Dirección invalida'
            if es_mayus(i) and es_mayus(anterior):
                direccion = 'Dirección invalida'
            anterior = i
        return direccion


    if control == 'Hard Control':
        direccion = direccion_hc()

    cp = borrar_espacios(cp)

    if pcp == 0:
        primer_cp = cp
        pcp += 1

    if primer_cp == cp:
        cant_primer_cp += 1
    
    if direccion == 'Dirección invalida':
        cedinvalid += 1
        continue

    cedvalid += 1


    # Determinar el destino en base al formato del cp
    def formato_cp(cp):
        # Aca utilizamos comprehensions para ahorrar el esquema del for
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
        global ccc, cce, ccs
        if tipo == 0 or tipo == 1 or tipo == 2:
            ccs += 1
        elif tipo == 3 or tipo == 4:
            ccc += 1
        else:
            cce += 1

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


    inicial = int(precio_inicial())


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
    imp_acu_total += int(final)

    #  Importe menor pagado por envios a Brasil
    if destino == 'Brasil':
        if antmenimp == None or antmenimp > final:
            mencp = cp
            menimp = final
            antmenimp = menimp

    if destino != 'Argentina':
        count_env_exterior += 1

    if destino == 'Argentina':
        if cp[0] == 'B':
            acc_arg_ba += final
            count_arg_ba += 1

tipo_mayor = max(ccc, ccs, cce)

if tipo_mayor == ccs:
    tipo_mayor = 'Carta Simple'
elif tipo_mayor == ccc:
    tipo_mayor = 'Carta Certificada'
else:
    tipo_mayor = 'Carta Expresa'

count_total_envios = cedvalid + cedinvalid
if count_total_envios >= 1:
    porc = (count_env_exterior * 100) // count_total_envios
else:
    porc = None

if count_arg_ba >= 1:
    prom = acc_arg_ba // count_arg_ba
else:
    prom = None


def results():
    print(' (r1) - Tipo de control de direcciones:', control)
    print(' (r2) - Cantidad de envios con direccion valida:', cedvalid)
    print(' (r3) - Cantidad de envios con direccion no valida:', cedinvalid)
    print(' (r4) - Total acumulado de importes finales:', int(imp_acu_total))
    print(' (r5) - Cantidad de cartas simples:', ccs)
    print(' (r6) - Cantidad de cartas certificadas:', ccc)
    print(' (r7) - Cantidad de cartas expresas:', cce)
    print(' (r8) - Tipo de carta con mayor cantidad de envios:', tipo_mayor)
    print(' (r9) - Codigo postal del primer envio del archivo:', primer_cp)
    print('(r10) - Cantidad de veces que entro ese primero:', cant_primer_cp)
    print('(r11) - Importe menor pagado por envios a Brasil:', int(menimp))
    print('(r12) - Codigo postal del envio a Brasil con importe menor:', mencp)
    print('(r13) - Porcentaje de envios al exterior sobre el total:', porc)
    # No toma CABA porque el runner asi indicaba
    print('(r14) - Importe final promedio de los envios a Buenos Aires:', int(prom))


results()