
#Escriba una función llamada rectángulo que tome dos números enteros m y n como argumentos e imprima
#saca un cuadro m × n que consta de asteriscos. A continuación se muestra la salida del rectángulo (2,4)

def rectangulo(m, n):
    for _ in range(m):  # Repite para cada fila
        for _ in range(n):  # Imprime asteriscos en cada columna
            print("*", end=" ")
        print()  # Salto de línea para pasar a la siguiente fila

# Ejemplo de uso:
alto = int(input("Ingrese el alto del rectángulo: "))                   #VOLVERLO A HACER
ancho = int(input("Ingrese el ancho del rectángulo: "))
rectangulo(alto, ancho)
