import random

# (a) Función para elegir aleatoriamente una ubicación vacía y colocar un "2" en ella.
def colocar_dos_aleatoriamente(tablero):
    filas = len(tablero)
    columnas = len(tablero[0])
    opciones = []

    # Encuentra todas las ubicaciones vacías en el tablero.
    for fila in range(filas):
        for columna in range(columnas):
            if tablero[fila][columna] == 0:
                opciones.append((fila, columna))

    if opciones:
        fila, columna = random.choice(opciones)
        tablero[fila][columna] = 2

# (b) Función para verificar si alguien ha ganado en el tablero.
def verificar_ganador(tablero):
    # Verificar filas
    for fila in tablero:
        if fila[0] == fila[1] == fila[2] and fila[0] != 0:
            return True

    # Verificar columnas
    for columna in range(3):
        if tablero[0][columna] == tablero[1][columna] == tablero[2][columna] and tablero[0][columna] != 0:
            return True

    # Verificar diagonales
    if tablero[0][0] == tablero[1][1] == tablero[2][2] and tablero[0][0] != 0:
        return True
    if tablero[0][2] == tablero[1][1] == tablero[2][0] and tablero[0][2] != 0:
        return True

    return False

# Ejemplo de uso
tablero = [
    [1, 0, 2],
    [0, 1, 0],
    [2, 0, 1]
]

# (a) Colocar un "2" aleatoriamente en el tablero.
colocar_dos_aleatoriamente(tablero)
print("Tablero con un '2' añadido:")
for fila in tablero:
    print(fila)

# (b) Verificar si alguien ha ganado en el tablero.
if verificar_ganador(tablero):
    print("¡Hay un ganador!")
else:
    print("No hay un ganador todavía.")
