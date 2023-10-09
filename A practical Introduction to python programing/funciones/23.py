def sudoku_resuelto_correctamente(sudoku):
    # Función para verificar si un Sudoku de 9 × 9 está resuelto correctamente.
    
    # Verificar filas
    for fila in sudoku:
        if len(set(fila)) != 9:
            return False  # Hay números repetidos en una fila.

    # Verificar columnas
    for columna in range(9):
        numeros_columna = set()
        for fila in range(9):
            numero = sudoku[fila][columna]
            if numero in numeros_columna:
                return False  # Hay números repetidos en una columna.
            numeros_columna.add(numero)

    # Verificar bloques
    for bloque_fila in range(3):
        for bloque_columna in range(3):
            numeros_bloque = set()
            for fila in range(3):
                for columna in range(3):
                    numero = sudoku[bloque_fila * 3 + fila][bloque_columna * 3 + columna]
                    if numero in numeros_bloque:
                        return False  # Hay números repetidos en un bloque.
                    numeros_bloque.add(numero)

    return True  # El Sudoku está resuelto correctamente.

# Ejemplo de uso
sudoku_correcto = [
    [5, 3, 4, 6, 7, 8, 9, 1, 2],
    [6, 7, 2, 1, 9, 5, 3, 4, 8],
    [1, 9, 8, 3, 4, 2, 5, 6, 7],
    [8, 5, 9, 7, 6, 1, 4, 2, 3],
    [4, 2, 6, 8, 5, 3, 7, 9, 1],
    [7, 1, 3, 9, 2, 4, 8, 5, 6],
    [9, 6, 1, 5, 3, 7, 2, 8, 4],
    [2, 8, 7, 4, 1, 9, 6, 3, 5],
    [3, 4, 5, 2, 8, 6, 1, 7, 9]
]

sudoku_incorrecto = [
    [5, 3, 4, 6, 7, 8, 9, 1, 2],
    [6, 7, 2, 1, 9, 5, 3, 4, 8],
    [1, 9, 8, 3, 4, 2, 5, 6, 7],
    [8, 5, 9, 7, 6, 1, 4, 2, 3],
    [4, 2, 6, 8, 5, 3, 7, 9, 1],
    [7, 1, 3, 9, 2, 4, 8, 5, 6],
    [9, 6, 1, 5, 3, 7, 2, 8, 4],
    [2, 8, 7, 4, 1, 9, 6, 3, 5],
    [3, 4, 5, 2, 8, 6, 1, 7, 4]  # Error en la última fila
]

if sudoku_resuelto_correctamente(sudoku_correcto):
    print("El Sudoku está resuelto correctamente.")
else:
    print("El Sudoku contiene errores.")

if sudoku_resuelto_correctamente(sudoku_incorrecto):
    print("El Sudoku está resuelto correctamente.")
else:
    print("El Sudoku contiene errores.")
