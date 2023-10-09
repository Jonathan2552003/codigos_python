# Diamante, permita al usuario el alto del diamante

alto = int(input("Ingrese el alto del diamante:   "))

for i in range(1, (alto + 1)):
    x = " " * (alto - i) + "*" * (
        2 * i - 1
    )  # El (2*i-1) Es para generar numeros impares que el lo que caracteriza al diamante
    print(x)

for j in range(alto - 1, 0, -1):
    x = " " * (alto - j) + "*" * (2 * j - 1)

    print(x)
