# Pedir al usuario el ancho y el alto de la caja
ancho = int(input("Ingrese el ancho de la caja: "))
alto = int(input("Ingrese el alto de la caja: "))

# Imprimir la parte superior de la caja
for i in range(ancho):  # Imprime la primera parte de la caja
    print("*", end=" ")
print()  # Se supone que es para imprimir una linea en blanco despues de imprimir toda la primera linea

# Imprimir los lados de la caja (sin contar las esquinas)
for i in range(
    alto - 2
):  # Imprime los lados y el -2 es porque ya se imprimieron en la parte superior e inferior
    print("*", end=" ")  # Imprime en la misma linea de seguido
    for j in range(
        ancho - 2
    ):  # Dentro del ciclo imprimira el "Relleno" de la caja que son espacios en blanco y -2 es por que los dos lados se acaban de imprimir
        print(" ", end=" ")  # El relleno de la caja son espacios vacios
    print("*")  # Luego imrpime otro asterisco al final de la linea

# 5Imprimir la parte inferior de la caja
if alto > 1:
    for i in range(ancho):
        print("*", end=" ")
    print()
