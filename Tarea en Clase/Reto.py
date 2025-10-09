# Codigo Reto 1

def presion_a_altitud(presion_hpa):
    # Tupla con las constantes.
    constantes = (44330, 1013.25, 5.255)
    return constantes[0] * (1 - (presion_hpa / constantes[1]) ** (1 / constantes[2]))

# Variables iniciales
primera_iteracion = True
dt = 1  # intervalo fijo de 1 segundo.

# Lista para almacenar los historiales.
historial = []  # cada elemento será un diccionario con los datos de una iteración.

while True:
    entrada = input("Ingrese presión barométrica en hPa (o 'salir'): ")

    if entrada.lower() == "salir":
        print("Programa finalizado.")
        print("\nHistorial de mediciones:")
        
        contador = 1
        for registro in historial:
            print(f"{contador}. Presión: {registro['presion']} hPa, Altitud: {registro['altitud']:.2f} m, "
                  f"Velocidad vertical: {registro['velocidad']:.2f} m/s")
            contador += 1
        break

    # Validar que la entrada sea un número.
    if entrada.replace(".", "").isdigit():
        presion = float(entrada)
    else:
        print("Entrada inválida. Intente de nuevo.")
        continue

    # Calcular altitud.
    altitud = presion_a_altitud(presion)

    # Si es la primera iteración, no hay velocidad previa.
    if primera_iteracion:
        velocidad_vertical = 0
        primera_iteracion = False
    else:
        # Calcular velocidad vertical usando la última altitud registrada.
        altitud_anterior = historial[-1]['altitud']
        velocidad_vertical = (altitud - altitud_anterior) / dt

    # Mostrar resultados.
    print(f"Altitud: {altitud:.2f} m, Velocidad vertical: {velocidad_vertical:.2f} m/s")

    # Guardar los datos en un diccionario dentro de la lista.
    registro = {
        "presion": presion,
        "altitud": altitud,
        "velocidad": velocidad_vertical
    }
    historial.append(registro)