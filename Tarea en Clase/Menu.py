# Menu en el que 1 ejecute el problema de Reto.py y 2 salga
import Reto

def menu():
    print("1. Ejecutar Reto")
    print("2. Salir")

while True:
    menu()
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        Reto.presion_a_altitud()
    elif opcion == "2":
        print("Saliendo...")
        break
    else:
        print("Opción no válida. Intente de nuevo.")