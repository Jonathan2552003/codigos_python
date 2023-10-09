# Ancho y alto de una caja de *
ancho = int(input("Ingrese el ancho de la caja"))
alto = int(input("Ingrese el alto de la caja"))

for i in range(alto):
    x = "*" * ancho
    print(x)
