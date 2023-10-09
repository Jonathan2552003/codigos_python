# Triangulo al reves
alto = int(input("Ingrese el alto de triangulo"))

for i in range((alto), 1, -1):
    alto = "*" * i
    print(alto)
