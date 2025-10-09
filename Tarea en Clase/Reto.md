## ESTE ARCHIVO TIENE COMO PROPÓSITO DEJAR UN ANÁLISIS SOBRE EL RETO ORIGINAL ANTES DE REALIZAR LOS CAMBIOS NECESARIOS##

## CÓDIGO HECHO: https://vscode.dev/github/hacUPB/prog-2025-2-4pm-u4-SamuelMejiaBravo/blob/main

# Codigo Reto 1

def presion_a_altitud(presion_hpa):
    # Fórmula barométrica simplificada
    ## Podemos poner una tupla aquí para guardar las constantes.
    return 44330 * (1 - (presion_hpa / 1013.25) ** (1/5.255))

# Variables iniciales
primera_iteracion = True
altitud_anterior = 0
dt = 1  # intervalo fijo de 1 segundo

## Aquí se puede poner una lista vacía para almacenar los historiales. También una lista de diccionarios para guardar resultados de cada iteración.

while True:
    entrada = input("Ingrese presión barométrica en hPa (o 'salir'): ")

    if entrada.lower() == "salir":
        print("Programa finalizado.")
        
        ## Aquí se puede poner una lista de diccionarios para en un futuro imprimir todos los historiales.
        break

    # Validar que la entrada sea un número
    if entrada.replace(".", "").isdigit():
        presion = float(entrada)
    else:
        print("Entrada inválida. Intente de nuevo.")
        continue

    # Calcular altitud
    altitud = presion_a_altitud(presion)

    ## Acá podemos poner una lista que guarde los datos de altitudes.

    if primera_iteracion:
        print(f"Altitud: {altitud:.2f} m")
        altitud_anterior = altitud
        primera_iteracion = False
    else:
        velocidad_vertical = (altitud - altitud_anterior) / dt
        print(f"Altitud: {altitud:.2f} m, Velocidad vertical: {velocidad_vertical:.2f} m/s")

        ## Se puede poner un diccionario con todos los datos de la iteración por si se necesita revisar el funcionamiento.

        ## Con una lista podría usar altitudes [-1] en vez de altitud anterior, esto simplifica todo el proceso.


        ##Uso de IA: Utilizamos IA para entender cómo podríamos incluír las nuevas cosas en el código. Ya luego nosotros miramos el código y decidimos dónde poner cada una.