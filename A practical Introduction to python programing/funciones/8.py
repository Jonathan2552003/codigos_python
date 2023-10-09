def numero_factores(n):
    contador = 0 
    for i in range(1, n+1):
        if n%i == 0:
            contador+=1
    return contador
    
x = int(input("Ingrese un numero:  "))
res = numero_factores(x)
print("El numero de factores es: ", res)