def base20(n):
    cadena = ""  # Para almacenar los números convertidos en letras
    while n > 0:
        residuo = n % 20
        # Convierte el residuo en su equivalente en letras (a=0, b=1, c=2, ...)
        letra = chr(ord('a') + residuo)
        cadena = letra + cadena  # Agrega la letra al principio de la cadena
        n = n // 20  # Divide n por 20

    return cadena

w = 45
res = base20(w)
print(f"El número {w} en base 20 es: {res}")