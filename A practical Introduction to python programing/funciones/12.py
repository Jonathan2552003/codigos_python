#Imprimir una lista de las posiciones de donde se encuentra el caracter "a"
def encontrar(cadena, caracter):
    lista_contadora = []
    for i in range (len(cadena)):
        if cadena[i] == caracter:
            lista_contadora.append(i)
    return lista_contadora                                  #Estudiarlo

cadena = "Hola"
caracter = "a"
res = encontrar(cadena, caracter)
print(res)


