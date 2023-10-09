#Saque el numero mas grande de la lista comparelo con un numero dado, si es menor o igual al numero imprimalo, de lo contrario saque otro
def mas_cercana(numero, lista):
    mayor = max(lista)
    while mayor > numero:
        lista.remove(mayor)
        mayor = max(lista)
    return mayor
x = 9                                 ###ASPERO, NOS SALIO BIEN
y = [1, 3, 10, 15, 50, 10, 20, 7]
re = mas_cercana(x,y)
print(re)