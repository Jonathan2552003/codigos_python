import random

def numero_aleatorio(n):

    lista = list(str(n))
    x = len(lista)
    rango_infreior = 10**(x-1)
    rango_superior = (10**x) - 1 
    numero_alea= random.randint(rango_infreior, rango_superior)
    return numero_alea

n = input("Ingrese un numero:   ")          #Necesitamos un porquito de ayuda en como definir los rangos pero vamos mejorando
resultado = numero_aleatorio(n)
print(resultado)
