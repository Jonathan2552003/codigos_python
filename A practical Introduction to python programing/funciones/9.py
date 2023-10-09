#Tome un numero y vuelva una lista de factores

def factores(n):
    lista = []
    for i in range(1, n+1):
        if n%i == 0:
            lista.append(i)
    return lista
numero = int(input("Ingrese un numero:  "))
x = factores(numero)
print(x)


