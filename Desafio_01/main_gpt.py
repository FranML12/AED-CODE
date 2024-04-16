# Programa realizado con chatGPT. Ingrese a este enlace para ver la conversacion:
# https://chat.openai.com/share/79c35227-a71d-4f88-a3ce-3be2c9df4d2e

def segundos_a_hhmmss(segundos):
    horas = segundos // 3600
    if horas > 24:
        return "Excedido"
    segundos %= 3600
    minutos = segundos // 60
    segundos %= 60
    return f"{horas:02d}:{minutos:02d}:{segundos:02d}"

def hhmmss_a_segundos(horas, minutos, segundos):
    if horas > 24:
        return "Excedido"
    return horas * 3600 + minutos * 60 + segundos

# Conversión de segundos a hh:mm:ss
segundos_input = int(input("Ingresa la cantidad de segundos a convertir: "))
print(f"{segundos_a_hhmmss(segundos_input)} son {segundos_input} segundos")

# Conversión de hh:mm:ss a segundos
horas_input = int(input("Ingresa las horas: "))
minutos_input = int(input("Ingresa los minutos: "))
segundos_input = int(input("Ingresa los segundos: "))
total_segundos = hhmmss_a_segundos(horas_input, minutos_input, segundos_input)
if isinstance(total_segundos, int):
    print(f"{horas_input:02d}:{minutos_input:02d}:{segundos_input:02d} son {total_segundos} segundos")
else:
    print(total_segundos)