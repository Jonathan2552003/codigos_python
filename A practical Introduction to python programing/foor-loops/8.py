# Escriba un programa que le pregunte al usuario su nombre y cuántas veces imprimirlo. El programa debe imprimir el nombre del usuario la cantidad especificada de veces.
nombre = input("Ingrese su nombre")
n = int(input("Cuantas veces quiere imprimirlo"))

for i in range(n):
    print(nombre)
