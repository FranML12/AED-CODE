# Archivo de funciones a importar a main
def es_letra(c):
    return 'A' <= c <= 'Z' or 'a' <= c <= 'z'


def es_mayus(c):
    return 'A' <= c <= 'Z'


def es_digito(c):
    return '0' <= c <= '9'


def borrar_espacios(rango):
    resultado = ''
    for i in rango:
        if i != ' ':
            resultado += i
    return resultado

def borrar_puntos(rango):
    resultado = ''
    for i in rango:
        if i != '.':
            resultado += i
    return resultado

def verificador(n:int,lower:int,upper:int):
    if lower <= n <= upper:
        return n 
    else:
        return None


def pais(cp):
    if len(cp) == 9 and cp[5] == '-' and es_letra(cp[:5]) and es_letra(cp[6:]):
        pais = 'Brasil'
    elif len(cp) == 8 and es_letra(cp[0]) and es_letra(cp[5:]) and es_digito(cp[1:5]):
        pais = 'Argentina'
    elif es_digito(cp):
        if len(cp) == 7:
            pais = 'Chile'
        elif len(cp) == 6:
            pais = 'Paraguay'
        elif len(cp) == 5:
            pais = 'Uruguay'
            if cp[0] == '1':
                pais = 'Montevideo'
        elif len(cp) == 4:
            pais = 'Bolivia'
        else:
            pais = 'Otros países'
    else:
        pais = 'Otros países'
        
    return pais

def final_amount(cp, destino, tipo, pago):
    # determinación del importe inicial a pagar.
    importes = (1100, 1800, 2450, 8300, 10900, 14300, 17900)
    monto = importes[tipo]

    if destino == 'Argentina':
        inicial = monto
    else:
        if destino == 'Bolivia' or destino == 'Paraguay' or (destino == 'Uruguay' and cp[0] == '1'):
            inicial = int(monto * 1.20)
        elif destino == 'Chile' or (destino == 'Uruguay' and cp[0] != '1'):
            inicial = int(monto * 1.25)
        elif destino == 'Brasil':
            if cp[0] == '8' or cp[0] == '9':
                inicial = int(monto * 1.20)
            else:
                if cp[0] == '0' or cp[0] == '1' or cp[0] == '2' or cp[0] == '3':
                    inicial = int(monto * 1.25)
                else:
                    inicial = int(monto * 1.30)
        else:
            inicial = int(monto * 1.50)

    # determinación del valor final del ticket a pagar.
    # asumimos que es pago en tarjeta...
    final = inicial

    # ... y si no lo fuese, la siguiente será cierta y cambiará el valor...
    if pago == 1:
        final = int(0.9 * inicial)

    return final

def check_dir(direccion):
    
    cl = cd = 0
    td = False
    ant = " "
    for car in direccion:
        if car in " .":
            # fin de palabra...
            # un flag si la palabra tenia todos sus caracteres digitos...
            if cl == cd:
                td = True

            # resetear variables de uso parcial...
            cl = cd = 0
            ant = " "

        else:
            # en la panza de la palabra...
            # contar la cantidad de caracteres de la palabra actual...
            cl += 1

            # si el caracter no es digito ni letra, la direccion no es valida... salir con False...
            if not car.isdigit() and not car.isalpha():
                return False

            # si hay dos mayusculas seguidas, la direccion no es valida... salir con False...
            if ant.isupper() and car.isupper():
                return False

            # contar digitos para saber si hay alguna palabra compuesta solo por digitos...
            if car.isdigit():
                cd += 1

            ant = car

    # si llegamos acá, es porque no había dos mayusculas seguidas y no habia caracteres raros...
    # ... por lo tanto, habria que salir con True a menos que no hubiese una palabra con todos digitos...
    return td

""" def valida_para_hc(destino):
    for i in range(len(destino)):
        car = destino[i]
        mayuscula_antes = False
        hay_dos_may_consecutivas = False 
        benditas_palabras = ""
        palabras_y_digitos_pa = False

        if not (('a'<= car <= 'z') or ('A'<= car <= 'Z') or ('0'<= car <= '9') or car == ' '):
            return False
        if ('A'<= car <= 'Z'):
            if mayuscula_antes:
                hay_dos_may_consecutivas = True
                break
            mayuscula_antes = True
        else: 
            mayuscula_antes = False
        if car != ' ':
            benditas_palabras += car
        else: 
            if len(benditas_palabras) > 0 and es_letra(benditas_palabras):
                palabras_y_digitos_pa = True
        benditas_palabras = ""
    if len(benditas_palabras) > 0 and es_letra(benditas_palabras):
        palabras_y_digitos_pa = True
    if palabras_y_digitos_pa and not hay_dos_may_consecutivas:
        return True
    else:
        return False """

def valida_para_hc(envios):
    # Esta lista almacenará los envíos con direcciones válidas
    envios_validos = []

    # Recorrer cada envío
    for envio in envios:
        destino = envio.destino
        mayuscula_antes = False
        hay_dos_may_consecutivas = False
        tiene_palabra_numerica = False
        palabra_actual = []
        print(destino)
        
        for car in destino:
            if car.isalpha() or car.isdigit() or car == ' ':
                # Verificar si hay dos mayúsculas consecutivas
                if car.isupper():
                    if mayuscula_antes:
                        hay_dos_may_consecutivas = True
                        break
                    mayuscula_antes = True
                else:
                    mayuscula_antes = False
                
                # Acumular caracteres de la palabra actual
                if car != ' ':
                    palabra_actual.append(car)
                else:
                    # Verificar si la palabra actual es numérica
                    if len(palabra_actual) > 0 and all(c.isdigit() for c in palabra_actual):
                        tiene_palabra_numerica = True
                    palabra_actual = []
            else:
                # Si hay un carácter no válido, el envío no pasa la validación
                hay_dos_may_consecutivas = True
                break

        # Verificar la última palabra acumulada
        if len(palabra_actual) > 0 and all(c.isdigit() for c in palabra_actual):
            tiene_palabra_numerica = True

        # Validar si cumple todas las condiciones
        if not hay_dos_may_consecutivas and tiene_palabra_numerica:
            envios_validos.append(envio)

    return envios_validos