# Numeros de fibonacci
n = int(
    input(
        "Ingrese cuantos numeros de fib quiere imprimir(Numero debe ser mayor o igual a dos):   "
    )
)

if n < 1 or n == 1:
    print("Su numero no es valido")

else:
    c, a, b = 0, 1, 1
    print(c, end=",")
    print(a, end=",")
    print(b, end=",")

    for i in range(2, n):
        siguiente_numero = a + b
        print(a + b, end=",")
        a = b
        b = siguiente_numero
