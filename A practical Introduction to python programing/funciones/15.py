def raiz(x,n):

    return x**(1/n)

w = float(input("Ingrese un numero para sacarle raiz"))
l = int(input("Ingrese el indice de la raiz "))
res = raiz(w,l)
print(res)