class Envio:
    def __init__(self, cp: str, destino: str, tipo: int, pago: int):
        self.codigo_postal = cp
        self.destino = destino
        self.tipo_envio = tipo
        self.forma_pago = pago
#inicializo la clase de envios y agregro los objetos respectivos y les asigno las variables de los futuros atributos
    def __str__(self) -> str:
        return f"{self.codigo_postal}, {self.destino}, {self.tipo_envio}, {self.forma_pago}"
#escribo el __str__ para cuando se quiera printear o coso 


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


def HC(registro):
    el_papu = []
    for l in range(len(registro)):
        destino = registro[l].destino
        menem = True
        for j in destino:
            if not (es_letra(j) or es_digito(j)):
                menem = False
            if es_mayus(j) and es_mayus(destino[destino.index(j)-1]):
                menem = False
        if menem:
            el_papu.append(registro[l])
    return el_papu

def control(data_line):
    if 'HC' in data_line:
        return 'Hard Control'
    elif 'SC' in data_line:
        return 'Soft Control'
    return 'Tipo de control desconocido'

def borrar_puntos(rango):
    resultado = ''
    for i in rango:
        if i != '.':
            resultado += i
    return resultado

def ordenamiento_cp(registro):
    n = len(registro)
    # Ordenamiento 
    for i in range(n - 1):
        ordenado = True
        for j in range(n - i - 1):
            if registro[j].codigo_postal > registro[j + 1].codigo_postal:
                # Intercambia los objetos si el código postal es mayor
                registro[j], registro[j + 1] = registro[j + 1], registro[j]
                ordenado = False
        if ordenado:
            break  # Si ya está ordenado, termina el ciclo
        