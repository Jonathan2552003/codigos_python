# Bucle para imptimir un triangulo el usuario especifica el alto del triangulo
alto = int(input("Ingrese el alto del triangulo"))

for i in range(1, alto + 1):
    alto = "*" * i
    print(alto)
