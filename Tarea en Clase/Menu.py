                                                            ### Menú Trabajo en clase ###
                                            # Para utilizarlo es necesario que escoja entre estas opciones: 
# Opción 1 ejecuta el problema de Reto.py 
# Opción 2, imprime el contenido de la lista 
# Opción 3, imprime los datos del diccionario; 
# Opción 4, sale.
import Reto    # Traigo el reto como módulo para poder ser usado en ese archivo.

def menu():    # Defino la función del Menú.
    print("\n1. Ejecutar Reto.py.")
    print("2. Imprimir datos de la lista.")
    print("3. Imprimir datos del diccionario.")
    print("4. Salir.")

    while True:
        opcion = input("Seleccione una opción (1-4): ")

        if opcion == '1':
            Reto.main()
        elif opcion == '2':
            print("Contenido de la lista:")
            for item in Reto.historial:
                print(item)
        elif opcion == '3':
            print("Contenido del diccionario:") # Como quedó mal la lista y terminan siendo lo mismo el diccionario y la lista, hacen lo mismo la opción 3 y la opción 4.
            for registro in Reto.historial:
                print(registro)
        elif opcion == '4':
            print("Saliendo del programa.")
            break
        else:
            print("Opción inválida, elija uno de los números indicados: ") #Evita que se pongan números diferentes del rango [1, 4].

menu() # Esto es para que pueda ejecutarse el menú sin que se ejecute automáticamente reto.py.