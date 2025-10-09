# Tupla vacía
coordenada = ()

# Tupla con elementos
coordenada = (33.9425, -118.4081)  # LAX (Aeropuerto de Los Ángeles)
# coordenada[0] = 43.9 Es un error por que la tupla es inmutable
#print(coordenda)
# Tupla con un solo elemento (requiere coma al final)
rumbo = (270,)  # Sin la coma sería tratado como un entero entre paréntesis

# Tupla sin paréntesis (empaquetado implícito)
avion_info = "Boeing 787", "Dreamliner", 2009, 242


# Indexación (similar a las listas)
print(coordenada[0])  # 33.9425
print(avion_info[-1])  # 242 (pasajeros)

# Slicing
print(avion_info[0:2])  # ("Boeing 787", "Dreamliner")

# Desempaquetado de tuplas
fabricante, modelo, año, capacidad = avion_info
print(f"El {fabricante} {modelo} se lanzó en {año}")

# Desempaquetado con *
lat, lon = coordenada
print(f"Latitud: {lat}, Longitud: {lon}")


lista_de_tuplas = [(0,0), (3,5), (8,3), (1,1)]
print(lista_de_tuplas)
lista_de_tuplas.append((45,6))
print(lista_de_tuplas) 
lista_de_tuplas[0] = (1,1) 
print(lista_de_tuplas)
lista_de_tuplas[2] = "palabra"
print(lista_de_tuplas)

tupla_de_listas = ([2,4,3], [9,6,12])
tupla_de_listas[1][0] = 18
print(tupla_de_listas)